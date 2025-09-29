"""
SQLite Connection Pool for improved performance and concurrency.

This module implements a connection pool to address SQLite locking issues
and improve performance for concurrent access patterns.
"""

import sqlite3
import threading
import time
import queue
import logging
from typing import Optional, Dict, Any, Callable, ContextManager
from contextlib import contextmanager
from dataclasses import dataclass
import os


@dataclass
class PoolConfig:
    """Configuration for connection pool."""
    max_connections: int = 10
    min_connections: int = 2
    connection_timeout: float = 30.0
    max_retries: int = 3
    retry_delay: float = 0.1
    idle_timeout: float = 300.0  # 5 minutes
    enable_wal_mode: bool = True
    busy_timeout: int = 30000  # 30 seconds
    enable_foreign_keys: bool = True


class PooledConnection:
    """Wrapper for pooled SQLite connections."""

    def __init__(self, db_path: str, config: PoolConfig):
        self.db_path = db_path
        self.config = config
        self.connection = None
        self.last_used = time.time()
        self.in_use = False
        self.created_at = time.time()
        self._lock = threading.Lock()

        # Create the connection
        self._create_connection()

    def _create_connection(self):
        """Create and configure the SQLite connection."""
        self.connection = sqlite3.connect(
            self.db_path,
            timeout=self.config.busy_timeout / 1000.0,
            check_same_thread=False
        )

        # Configure connection settings
        self.connection.execute('PRAGMA busy_timeout = ?', (self.config.busy_timeout,))

        if self.config.enable_wal_mode:
            self.connection.execute('PRAGMA journal_mode = WAL')

        if self.config.enable_foreign_keys:
            self.connection.execute('PRAGMA foreign_keys = ON')

        # Performance optimizations
        self.connection.execute('PRAGMA synchronous = NORMAL')
        self.connection.execute('PRAGMA cache_size = -64000')  # 64MB cache
        self.connection.execute('PRAGMA temp_store = MEMORY')

        self.connection.row_factory = sqlite3.Row

    def acquire(self) -> sqlite3.Connection:
        """Acquire the connection for use."""
        with self._lock:
            if self.in_use:
                raise RuntimeError("Connection already in use")

            # Check if connection is still valid
            if not self._is_connection_valid():
                self._create_connection()

            self.in_use = True
            self.last_used = time.time()
            return self.connection

    def release(self):
        """Release the connection back to the pool."""
        with self._lock:
            self.in_use = False
            self.last_used = time.time()

    def close(self):
        """Close the connection."""
        with self._lock:
            if self.connection:
                try:
                    self.connection.close()
                except Exception:
                    pass
                self.connection = None

    def _is_connection_valid(self) -> bool:
        """Check if the connection is still valid."""
        if not self.connection:
            return False

        try:
            self.connection.execute('SELECT 1')
            return True
        except Exception:
            return False

    @property
    def is_idle(self) -> bool:
        """Check if connection has been idle too long."""
        return (not self.in_use and
                time.time() - self.last_used > self.config.idle_timeout)


class SQLiteConnectionPool:
    """Thread-safe SQLite connection pool."""

    def __init__(self, db_path: str, config: Optional[PoolConfig] = None):
        self.db_path = db_path
        self.config = config or PoolConfig()
        self._pool: queue.Queue[PooledConnection] = queue.Queue()
        self._all_connections: Dict[int, PooledConnection] = {}
        self._lock = threading.RLock()
        self._closed = False
        self._cleanup_thread = None

        # Ensure database directory exists
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

        # Initialize minimum connections
        self._initialize_pool()

        # Start cleanup thread
        self._start_cleanup_thread()

    def _initialize_pool(self):
        """Initialize the pool with minimum connections."""
        for _ in range(self.config.min_connections):
            try:
                conn = PooledConnection(self.db_path, self.config)
                self._pool.put(conn)
                self._all_connections[id(conn)] = conn
            except Exception as e:
                logging.error(f"Failed to create initial connection: {e}")

    def _start_cleanup_thread(self):
        """Start the cleanup thread for idle connections."""
        self._cleanup_thread = threading.Thread(
            target=self._cleanup_idle_connections,
            daemon=True
        )
        self._cleanup_thread.start()

    def _cleanup_idle_connections(self):
        """Clean up idle connections periodically."""
        while not self._closed:
            try:
                time.sleep(60)  # Check every minute
                self._remove_idle_connections()
            except Exception as e:
                logging.error(f"Error in cleanup thread: {e}")

    def _remove_idle_connections(self):
        """Remove connections that have been idle too long."""
        with self._lock:
            if self._closed:
                return

            # Don't go below minimum connections
            if len(self._all_connections) <= self.config.min_connections:
                return

            idle_connections = []
            for conn_id, conn in self._all_connections.items():
                if conn.is_idle:
                    idle_connections.append(conn_id)

            for conn_id in idle_connections:
                if len(self._all_connections) > self.config.min_connections:
                    conn = self._all_connections.pop(conn_id)
                    conn.close()

    @contextmanager
    def get_connection(self) -> ContextManager[sqlite3.Connection]:
        """Get a connection from the pool as a context manager."""
        if self._closed:
            raise RuntimeError("Connection pool is closed")

        pooled_conn = None
        retries = 0

        while retries < self.config.max_retries:
            try:
                # Try to get an available connection
                try:
                    pooled_conn = self._pool.get(timeout=self.config.connection_timeout)
                except queue.Empty:
                    # No available connections, try to create a new one
                    if len(self._all_connections) < self.config.max_connections:
                        pooled_conn = self._create_new_connection()
                    else:
                        # Pool is full, wait a bit and retry
                        time.sleep(self.config.retry_delay)
                        retries += 1
                        continue

                if pooled_conn:
                    conn = pooled_conn.acquire()
                    try:
                        yield conn
                    finally:
                        pooled_conn.release()
                        self._pool.put(pooled_conn)
                    return

            except Exception as e:
                if pooled_conn:
                    # Connection might be corrupted, remove it
                    self._remove_connection(pooled_conn)

                if retries < self.config.max_retries - 1:
                    time.sleep(self.config.retry_delay * (2 ** retries))  # Exponential backoff
                    retries += 1
                else:
                    raise ConnectionError(f"Failed to get connection after {self.config.max_retries} retries: {e}")

    def _create_new_connection(self) -> Optional[PooledConnection]:
        """Create a new connection if pool isn't full."""
        with self._lock:
            if len(self._all_connections) >= self.config.max_connections:
                return None

            try:
                conn = PooledConnection(self.db_path, self.config)
                self._all_connections[id(conn)] = conn
                return conn
            except Exception as e:
                logging.error(f"Failed to create new connection: {e}")
                return None

    def _remove_connection(self, pooled_conn: PooledConnection):
        """Remove a connection from the pool."""
        with self._lock:
            conn_id = id(pooled_conn)
            if conn_id in self._all_connections:
                del self._all_connections[conn_id]
            pooled_conn.close()

    def execute(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        """Execute a query and return the cursor."""
        with self.get_connection() as conn:
            return conn.execute(query, params)

    def executemany(self, query: str, params_list) -> sqlite3.Cursor:
        """Execute a query with multiple parameter sets."""
        with self.get_connection() as conn:
            return conn.executemany(query, params_list)

    def fetch_one(self, query: str, params: tuple = ()) -> Optional[sqlite3.Row]:
        """Execute query and fetch one result."""
        with self.get_connection() as conn:
            cursor = conn.execute(query, params)
            return cursor.fetchone()

    def fetch_all(self, query: str, params: tuple = ()) -> list:
        """Execute query and fetch all results."""
        with self.get_connection() as conn:
            cursor = conn.execute(query, params)
            return cursor.fetchall()

    def execute_transaction(self, operations: Callable[[sqlite3.Connection], Any]) -> Any:
        """Execute multiple operations in a transaction."""
        with self.get_connection() as conn:
            try:
                conn.execute('BEGIN TRANSACTION')
                result = operations(conn)
                conn.execute('COMMIT')
                return result
            except Exception:
                conn.execute('ROLLBACK')
                raise

    def get_stats(self) -> Dict[str, Any]:
        """Get connection pool statistics."""
        with self._lock:
            active_connections = sum(1 for conn in self._all_connections.values() if conn.in_use)
            idle_connections = len(self._all_connections) - active_connections

            return {
                'total_connections': len(self._all_connections),
                'active_connections': active_connections,
                'idle_connections': idle_connections,
                'max_connections': self.config.max_connections,
                'min_connections': self.config.min_connections,
                'pool_size': self._pool.qsize(),
                'is_closed': self._closed
            }

    def close(self):
        """Close the connection pool and all connections."""
        with self._lock:
            if self._closed:
                return

            self._closed = True

            # Close all connections
            for conn in self._all_connections.values():
                conn.close()

            self._all_connections.clear()

            # Clear the queue
            while not self._pool.empty():
                try:
                    self._pool.get_nowait()
                except queue.Empty:
                    break

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class PooledSQLiteStore:
    """SQLite store using connection pooling."""

    def __init__(self, db_path: str, pool_config: Optional[PoolConfig] = None):
        self.db_path = db_path
        self.pool = SQLiteConnectionPool(db_path, pool_config)
        self._initialize_schema()

    def _initialize_schema(self):
        """Initialize database schema."""
        # This would be implemented by subclasses
        pass

    def close(self):
        """Close the pooled store."""
        self.pool.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# Example usage in memory store
class PooledMemoryStore(PooledSQLiteStore):
    """Memory store using connection pooling."""

    def _initialize_schema(self):
        """Initialize memory store schema."""
        schema_queries = [
            '''CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                user_input TEXT NOT NULL,
                agent_output TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                metadata TEXT
            )''',

            '''CREATE INDEX IF NOT EXISTS idx_conversations_session
               ON conversations(session_id)''',

            '''CREATE INDEX IF NOT EXISTS idx_conversations_timestamp
               ON conversations(timestamp)'''
        ]

        for query in schema_queries:
            self.pool.execute(query)

    def add_conversation(self, session_id: str, user_input: str,
                        agent_output: str, metadata: Optional[Dict] = None):
        """Add a conversation to memory."""
        import json
        from datetime import datetime

        self.pool.execute(
            '''INSERT INTO conversations
               (session_id, user_input, agent_output, timestamp, metadata)
               VALUES (?, ?, ?, ?, ?)''',
            (session_id, user_input, agent_output,
             datetime.now().isoformat(),
             json.dumps(metadata) if metadata else None)
        )

    def get_conversation_history(self, session_id: str, limit: int = 50) -> list:
        """Get conversation history for a session."""
        return self.pool.fetch_all(
            '''SELECT * FROM conversations
               WHERE session_id = ?
               ORDER BY timestamp DESC
               LIMIT ?''',
            (session_id, limit)
        )