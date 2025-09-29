"""
LLM Response Caching System.

This module implements intelligent caching for LLM responses to improve
performance and reduce API costs.
"""

import hashlib
import json
import time
import os
import sqlite3
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
import threading
from contextlib import contextmanager

from ..memory.connection_pool import SQLiteConnectionPool, PoolConfig


@dataclass
class CacheConfig:
    """Configuration for response caching."""
    max_cache_size_mb: int = 500  # Maximum cache size in MB
    default_ttl_hours: int = 24   # Default time-to-live in hours
    max_ttl_hours: int = 168      # Maximum TTL (1 week)
    cleanup_interval_minutes: int = 60  # Cleanup frequency
    enable_compression: bool = True
    cache_hit_extend_ttl: bool = True  # Extend TTL on cache hits
    similarity_threshold: float = 0.85  # For fuzzy matching


@dataclass
class CacheEntry:
    """Represents a cached LLM response."""
    cache_key: str
    prompt_hash: str
    provider: str
    model: str
    prompt: str
    response: str
    metadata: Dict[str, Any]
    created_at: datetime
    expires_at: datetime
    access_count: int
    last_accessed: datetime
    compressed: bool = False
    tokens_used: Optional[int] = None
    cost_estimate: Optional[float] = None


class LLMResponseCache:
    """Intelligent LLM response caching system."""

    def __init__(self, cache_dir: str, config: Optional[CacheConfig] = None):
        self.cache_dir = cache_dir
        self.config = config or CacheConfig()
        self.db_path = os.path.join(cache_dir, "llm_cache.db")

        # Ensure cache directory exists
        os.makedirs(cache_dir, exist_ok=True)

        # Initialize connection pool
        pool_config = PoolConfig(
            max_connections=5,
            min_connections=1,
            enable_wal_mode=True
        )
        self.pool = SQLiteConnectionPool(self.db_path, pool_config)

        # Initialize schema
        self._initialize_schema()

        # Start cleanup thread
        self._cleanup_thread = None
        self._stop_cleanup = threading.Event()
        self._start_cleanup_thread()

    def _initialize_schema(self):
        """Initialize the cache database schema."""
        schema_queries = [
            '''CREATE TABLE IF NOT EXISTS cache_entries (
                cache_key TEXT PRIMARY KEY,
                prompt_hash TEXT NOT NULL,
                provider TEXT NOT NULL,
                model TEXT NOT NULL,
                prompt TEXT NOT NULL,
                response TEXT NOT NULL,
                metadata TEXT,
                created_at TEXT NOT NULL,
                expires_at TEXT NOT NULL,
                access_count INTEGER DEFAULT 0,
                last_accessed TEXT NOT NULL,
                compressed BOOLEAN DEFAULT FALSE,
                tokens_used INTEGER,
                cost_estimate REAL,
                response_size INTEGER
            )''',

            '''CREATE INDEX IF NOT EXISTS idx_cache_prompt_hash
               ON cache_entries(prompt_hash)''',

            '''CREATE INDEX IF NOT EXISTS idx_cache_provider_model
               ON cache_entries(provider, model)''',

            '''CREATE INDEX IF NOT EXISTS idx_cache_expires_at
               ON cache_entries(expires_at)''',

            '''CREATE INDEX IF NOT EXISTS idx_cache_created_at
               ON cache_entries(created_at)''',

            '''CREATE TABLE IF NOT EXISTS cache_stats (
                id INTEGER PRIMARY KEY,
                date TEXT NOT NULL,
                cache_hits INTEGER DEFAULT 0,
                cache_misses INTEGER DEFAULT 0,
                total_requests INTEGER DEFAULT 0,
                bytes_saved INTEGER DEFAULT 0,
                cost_saved REAL DEFAULT 0.0,
                UNIQUE(date)
            )'''
        ]

        for query in schema_queries:
            self.pool.execute(query)

    def _start_cleanup_thread(self):
        """Start the cleanup thread."""
        self._cleanup_thread = threading.Thread(
            target=self._periodic_cleanup,
            daemon=True
        )
        self._cleanup_thread.start()

    def _periodic_cleanup(self):
        """Periodically clean up expired entries."""
        while not self._stop_cleanup.wait(self.config.cleanup_interval_minutes * 60):
            try:
                self.cleanup_expired()
                self._enforce_size_limit()
            except Exception as e:
                print(f"Error in cache cleanup: {e}")

    def get(self, prompt: str, provider: str, model: str,
            temperature: float = 0.7, max_tokens: Optional[int] = None) -> Optional[CacheEntry]:
        """Get cached response for a prompt."""
        cache_key = self._generate_cache_key(prompt, provider, model, temperature, max_tokens)
        prompt_hash = self._hash_prompt(prompt)

        # First try exact match
        entry = self._get_exact_match(cache_key)
        if entry:
            self._update_access_stats(cache_key)
            self._record_cache_hit()
            return entry

        # Try fuzzy matching for similar prompts
        if self.config.similarity_threshold > 0:
            similar_entry = self._find_similar_entry(prompt_hash, provider, model)
            if similar_entry:
                self._update_access_stats(similar_entry.cache_key)
                self._record_cache_hit()
                return similar_entry

        self._record_cache_miss()
        return None

    def put(self, prompt: str, response: str, provider: str, model: str,
            temperature: float = 0.7, max_tokens: Optional[int] = None,
            metadata: Optional[Dict[str, Any]] = None,
            ttl_hours: Optional[int] = None,
            tokens_used: Optional[int] = None,
            cost_estimate: Optional[float] = None) -> str:
        """Cache an LLM response."""
        cache_key = self._generate_cache_key(prompt, provider, model, temperature, max_tokens)
        prompt_hash = self._hash_prompt(prompt)

        # Determine TTL
        ttl = ttl_hours or self.config.default_ttl_hours
        ttl = min(ttl, self.config.max_ttl_hours)

        created_at = datetime.now()
        expires_at = created_at + timedelta(hours=ttl)

        # Compress response if enabled and large
        compressed = False
        response_to_store = response
        if self.config.enable_compression and len(response) > 1000:
            response_to_store = self._compress_response(response)
            compressed = True

        # Store in database
        self.pool.execute(
            '''INSERT OR REPLACE INTO cache_entries
               (cache_key, prompt_hash, provider, model, prompt, response,
                metadata, created_at, expires_at, access_count, last_accessed,
                compressed, tokens_used, cost_estimate, response_size)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (
                cache_key, prompt_hash, provider, model, prompt, response_to_store,
                json.dumps(metadata) if metadata else None,
                created_at.isoformat(), expires_at.isoformat(),
                0, created_at.isoformat(), compressed,
                tokens_used, cost_estimate, len(response)
            )
        )

        return cache_key

    def _get_exact_match(self, cache_key: str) -> Optional[CacheEntry]:
        """Get exact cache match."""
        row = self.pool.fetch_one(
            '''SELECT * FROM cache_entries
               WHERE cache_key = ? AND expires_at > ?''',
            (cache_key, datetime.now().isoformat())
        )

        if row:
            return self._row_to_cache_entry(row)
        return None

    def _find_similar_entry(self, prompt_hash: str, provider: str, model: str) -> Optional[CacheEntry]:
        """Find similar cached entries using fuzzy matching."""
        # For now, use exact prompt hash matching
        # In future, could implement more sophisticated similarity matching
        rows = self.pool.fetch_all(
            '''SELECT * FROM cache_entries
               WHERE prompt_hash = ? AND provider = ? AND model = ?
               AND expires_at > ?
               ORDER BY access_count DESC, last_accessed DESC
               LIMIT 1''',
            (prompt_hash, provider, model, datetime.now().isoformat())
        )

        if rows:
            return self._row_to_cache_entry(rows[0])
        return None

    def _row_to_cache_entry(self, row) -> CacheEntry:
        """Convert database row to CacheEntry."""
        response = row['response']
        if row['compressed']:
            response = self._decompress_response(response)

        metadata = {}
        if row['metadata']:
            try:
                metadata = json.loads(row['metadata'])
            except json.JSONDecodeError:
                pass

        return CacheEntry(
            cache_key=row['cache_key'],
            prompt_hash=row['prompt_hash'],
            provider=row['provider'],
            model=row['model'],
            prompt=row['prompt'],
            response=response,
            metadata=metadata,
            created_at=datetime.fromisoformat(row['created_at']),
            expires_at=datetime.fromisoformat(row['expires_at']),
            access_count=row['access_count'],
            last_accessed=datetime.fromisoformat(row['last_accessed']),
            compressed=row['compressed'],
            tokens_used=row['tokens_used'],
            cost_estimate=row['cost_estimate']
        )

    def _update_access_stats(self, cache_key: str):
        """Update access statistics for a cache entry."""
        now = datetime.now()

        # Update access count and last accessed time
        self.pool.execute(
            '''UPDATE cache_entries
               SET access_count = access_count + 1,
                   last_accessed = ?
               WHERE cache_key = ?''',
            (now.isoformat(), cache_key)
        )

        # Extend TTL on cache hit if configured
        if self.config.cache_hit_extend_ttl:
            new_expires_at = now + timedelta(hours=self.config.default_ttl_hours)
            self.pool.execute(
                '''UPDATE cache_entries
                   SET expires_at = ?
                   WHERE cache_key = ? AND expires_at < ?''',
                (new_expires_at.isoformat(), cache_key, new_expires_at.isoformat())
            )

    def _generate_cache_key(self, prompt: str, provider: str, model: str,
                          temperature: float, max_tokens: Optional[int]) -> str:
        """Generate a unique cache key for the request."""
        key_data = {
            'prompt': prompt,
            'provider': provider,
            'model': model,
            'temperature': temperature,
            'max_tokens': max_tokens
        }

        key_string = json.dumps(key_data, sort_keys=True)
        return hashlib.sha256(key_string.encode()).hexdigest()

    def _hash_prompt(self, prompt: str) -> str:
        """Generate a hash for the prompt (for similarity matching)."""
        # Remove whitespace variations for better matching
        normalized_prompt = ' '.join(prompt.split())
        return hashlib.md5(normalized_prompt.encode()).hexdigest()

    def _compress_response(self, response: str) -> str:
        """Compress response text."""
        import gzip
        import base64

        compressed = gzip.compress(response.encode('utf-8'))
        return base64.b64encode(compressed).decode('ascii')

    def _decompress_response(self, compressed_response: str) -> str:
        """Decompress response text."""
        import gzip
        import base64

        compressed_data = base64.b64decode(compressed_response.encode('ascii'))
        return gzip.decompress(compressed_data).decode('utf-8')

    def cleanup_expired(self) -> int:
        """Remove expired cache entries."""
        cursor = self.pool.execute(
            '''DELETE FROM cache_entries WHERE expires_at <= ?''',
            (datetime.now().isoformat(),)
        )
        return cursor.rowcount

    def _enforce_size_limit(self):
        """Enforce cache size limits."""
        # Get current cache size
        total_size = self._get_cache_size_mb()

        if total_size > self.config.max_cache_size_mb:
            # Remove oldest entries until under limit
            entries_to_remove = self.pool.fetch_all(
                '''SELECT cache_key, response_size
                   FROM cache_entries
                   ORDER BY last_accessed ASC''')

            removed_size = 0
            for row in entries_to_remove:
                if total_size - (removed_size / 1024 / 1024) <= self.config.max_cache_size_mb:
                    break

                self.pool.execute(
                    'DELETE FROM cache_entries WHERE cache_key = ?',
                    (row['cache_key'],)
                )
                removed_size += row['response_size'] or 0

    def _get_cache_size_mb(self) -> float:
        """Get current cache size in MB."""
        row = self.pool.fetch_one(
            'SELECT SUM(response_size) as total_size FROM cache_entries'
        )
        total_bytes = row['total_size'] or 0
        return total_bytes / 1024 / 1024

    def _record_cache_hit(self):
        """Record a cache hit in statistics."""
        today = datetime.now().date().isoformat()
        self.pool.execute(
            '''INSERT OR IGNORE INTO cache_stats (date) VALUES (?)''',
            (today,)
        )
        self.pool.execute(
            '''UPDATE cache_stats
               SET cache_hits = cache_hits + 1,
                   total_requests = total_requests + 1
               WHERE date = ?''',
            (today,)
        )

    def _record_cache_miss(self):
        """Record a cache miss in statistics."""
        today = datetime.now().date().isoformat()
        self.pool.execute(
            '''INSERT OR IGNORE INTO cache_stats (date) VALUES (?)''',
            (today,)
        )
        self.pool.execute(
            '''UPDATE cache_stats
               SET cache_misses = cache_misses + 1,
                   total_requests = total_requests + 1
               WHERE date = ?''',
            (today,)
        )

    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        # Current cache stats
        cache_info = self.pool.fetch_one(
            '''SELECT COUNT(*) as entry_count,
                      SUM(response_size) as total_size,
                      AVG(access_count) as avg_access_count
               FROM cache_entries'''
        )

        # Recent stats (last 7 days)
        week_ago = (datetime.now() - timedelta(days=7)).date().isoformat()
        recent_stats = self.pool.fetch_one(
            '''SELECT SUM(cache_hits) as hits,
                      SUM(cache_misses) as misses,
                      SUM(total_requests) as total
               FROM cache_stats
               WHERE date >= ?''',
            (week_ago,)
        )

        hits = recent_stats['hits'] or 0
        misses = recent_stats['misses'] or 0
        total = recent_stats['total'] or 0

        hit_rate = (hits / total * 100) if total > 0 else 0

        return {
            'entry_count': cache_info['entry_count'] or 0,
            'total_size_mb': (cache_info['total_size'] or 0) / 1024 / 1024,
            'avg_access_count': cache_info['avg_access_count'] or 0,
            'cache_hits_7d': hits,
            'cache_misses_7d': misses,
            'hit_rate_7d': hit_rate,
            'max_size_mb': self.config.max_cache_size_mb,
            'size_utilization': ((cache_info['total_size'] or 0) / 1024 / 1024) / self.config.max_cache_size_mb * 100
        }

    def clear_cache(self, provider: Optional[str] = None, model: Optional[str] = None) -> int:
        """Clear cache entries, optionally filtered by provider/model."""
        if provider and model:
            cursor = self.pool.execute(
                '''DELETE FROM cache_entries WHERE provider = ? AND model = ?''',
                (provider, model)
            )
        elif provider:
            cursor = self.pool.execute(
                '''DELETE FROM cache_entries WHERE provider = ?''',
                (provider,)
            )
        else:
            cursor = self.pool.execute('DELETE FROM cache_entries')

        return cursor.rowcount

    def close(self):
        """Close the cache and cleanup resources."""
        if self._cleanup_thread:
            self._stop_cleanup.set()
            self._cleanup_thread.join(timeout=5)

        self.pool.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# Context manager for cached LLM calls
@contextmanager
def cached_llm_call(cache: LLMResponseCache, prompt: str, provider: str,
                   model: str, temperature: float = 0.7,
                   max_tokens: Optional[int] = None,
                   ttl_hours: Optional[int] = None):
    """Context manager for cached LLM calls."""
    # Try to get from cache first
    cached_entry = cache.get(prompt, provider, model, temperature, max_tokens)

    if cached_entry:
        yield cached_entry.response, True  # response, from_cache
    else:
        # Placeholder for actual LLM call
        # The calling code should make the LLM call and then cache the response
        response = yield None, False  # None response, not from cache

        if response:
            cache.put(
                prompt=prompt,
                response=response,
                provider=provider,
                model=model,
                temperature=temperature,
                max_tokens=max_tokens,
                ttl_hours=ttl_hours
            )