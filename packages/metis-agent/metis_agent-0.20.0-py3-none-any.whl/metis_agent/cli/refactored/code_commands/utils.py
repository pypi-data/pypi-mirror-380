"""
Utility functions for code commands.

This module contains helper functions and utilities used across
the code command modules.
"""

import re
from typing import Dict, Any, List, Optional, Tuple
import os


def determine_operation_mode(request_text: str, auto: bool = False, fast: bool = False,
                           stream: bool = False) -> str:
    """Determine the appropriate operation mode based on request and flags."""
    if auto:
        return 'auto'
    if fast:
        return 'fast'
    if stream:
        return 'stream'

    # Analyze request complexity
    complexity = assess_operation_complexity(request_text)

    if complexity == 'simple':
        return 'direct'
    elif complexity == 'medium':
        return 'balanced'
    elif complexity == 'complex':
        return 'thorough'
    else:
        return 'balanced'


def assess_operation_complexity(request_text: str) -> str:
    """Assess the complexity of the operation based on the request text."""
    request_lower = request_text.lower()

    # Complex operation indicators
    complex_indicators = [
        'architecture', 'design pattern', 'full implementation',
        'complete solution', 'entire project', 'from scratch',
        'comprehensive', 'detailed analysis', 'multiple files',
        'integration', 'deployment', 'production ready'
    ]

    # Medium complexity indicators
    medium_indicators = [
        'refactor', 'optimize', 'improve', 'enhance',
        'add feature', 'implement', 'create class',
        'write function', 'test', 'documentation'
    ]

    # Simple operation indicators
    simple_indicators = [
        'fix typo', 'rename variable', 'add comment',
        'format code', 'simple change', 'quick fix'
    ]

    # Count indicators
    complex_count = sum(1 for indicator in complex_indicators if indicator in request_lower)
    medium_count = sum(1 for indicator in medium_indicators if indicator in request_lower)
    simple_count = sum(1 for indicator in simple_indicators if indicator in request_lower)

    # Determine complexity
    if complex_count > 0 or len(request_text.split()) > 20:
        return 'complex'
    elif medium_count > 0 or len(request_text.split()) > 10:
        return 'medium'
    elif simple_count > 0 or len(request_text.split()) <= 5:
        return 'simple'
    else:
        return 'medium'


def determine_confirmation_level(operation_mode: str, yes: bool = False, review: bool = False) -> str:
    """Determine the confirmation level based on operation mode and flags."""
    if yes:
        return 'none'
    if review:
        return 'high'

    mode_to_confirmation = {
        'auto': 'none',
        'fast': 'low',
        'direct': 'low',
        'balanced': 'normal',
        'thorough': 'high',
        'stream': 'normal'
    }

    return mode_to_confirmation.get(operation_mode, 'normal')


def determine_interface_mode(interface_flag: Optional[str] = None,
                           user_experience_level: Optional[str] = None) -> str:
    """Determine the interface mode based on user preferences."""
    if interface_flag:
        return interface_flag

    # Default based on experience level
    if user_experience_level == 'beginner':
        return 'simple'
    elif user_experience_level == 'expert':
        return 'expert'
    else:
        return 'advanced'


def detect_subcommand_from_text(request_text: str) -> Optional[str]:
    """Detect if the request text matches any subcommand patterns."""
    request_lower = request_text.lower()

    # Subcommand patterns
    subcommand_patterns = {
        'project': [
            r'\bcreate\s+project\b', r'\bnew\s+project\b', r'\bproject\s+setup\b',
            r'\binitialize\s+project\b', r'\bscaffold\s+project\b'
        ],
        'test': [
            r'\bwrite\s+tests?\b', r'\bcreate\s+tests?\b', r'\bgenerate\s+tests?\b',
            r'\bunit\s+tests?\b', r'\btest\s+coverage\b', r'\btesting\b'
        ],
        'docs': [
            r'\bwrite\s+docs?\b', r'\bcreate\s+documentation\b', r'\bgenerate\s+docs?\b',
            r'\bapi\s+docs?\b', r'\breadme\b', r'\bdocumentation\b'
        ],
        'status': [
            r'\bproject\s+status\b', r'\bcheck\s+status\b', r'\bstatus\b'
        ]
    }

    for subcommand, patterns in subcommand_patterns.items():
        for pattern in patterns:
            if re.search(pattern, request_lower):
                return subcommand

    return None


def parse_git_branch_name(request_text: str) -> Optional[str]:
    """Parse potential git branch name from request text."""
    # Look for branch-like patterns
    branch_patterns = [
        r'feature[/-]([a-zA-Z0-9_-]+)',
        r'fix[/-]([a-zA-Z0-9_-]+)',
        r'hotfix[/-]([a-zA-Z0-9_-]+)',
        r'branch\s+([a-zA-Z0-9_-]+)',
        r'on\s+branch\s+([a-zA-Z0-9_-]+)'
    ]

    request_lower = request_text.lower()
    for pattern in branch_patterns:
        match = re.search(pattern, request_lower)
        if match:
            return match.group(1)

    return None


def extract_file_patterns(request_text: str) -> List[str]:
    """Extract file patterns and paths from request text."""
    # Common file extension patterns
    file_patterns = re.findall(r'\*\.[a-zA-Z0-9]+', request_text)

    # Direct file paths
    file_paths = re.findall(r'[a-zA-Z0-9_/-]+\.[a-zA-Z0-9]+', request_text)

    # Directory patterns
    dir_patterns = re.findall(r'[a-zA-Z0-9_/-]+/', request_text)

    return file_patterns + file_paths + dir_patterns


def extract_programming_languages(request_text: str) -> List[str]:
    """Extract mentioned programming languages from request text."""
    language_keywords = {
        'python': ['python', 'py', 'django', 'flask', 'fastapi'],
        'javascript': ['javascript', 'js', 'node', 'nodejs', 'react', 'vue', 'angular'],
        'typescript': ['typescript', 'ts'],
        'java': ['java', 'spring', 'maven', 'gradle'],
        'rust': ['rust', 'cargo'],
        'go': ['go', 'golang'],
        'php': ['php', 'laravel', 'symfony'],
        'ruby': ['ruby', 'rails'],
        'csharp': ['c#', 'csharp', 'dotnet', '.net'],
        'cpp': ['c++', 'cpp', 'cmake'],
        'swift': ['swift', 'ios'],
        'kotlin': ['kotlin', 'android'],
        'scala': ['scala'],
        'dart': ['dart', 'flutter'],
        'r': [' r ', 'rstats'],
        'julia': ['julia'],
        'sql': ['sql', 'database', 'postgres', 'mysql'],
        'html': ['html', 'html5'],
        'css': ['css', 'css3', 'scss', 'sass'],
        'shell': ['bash', 'shell', 'zsh', 'sh']
    }

    request_lower = request_text.lower()
    detected_languages = []

    for language, keywords in language_keywords.items():
        for keyword in keywords:
            if keyword in request_lower:
                if language not in detected_languages:
                    detected_languages.append(language)
                break

    return detected_languages


def extract_frameworks_and_tools(request_text: str) -> List[str]:
    """Extract mentioned frameworks and tools from request text."""
    frameworks_tools = {
        # Web frameworks
        'react', 'vue', 'angular', 'svelte', 'nextjs', 'nuxtjs', 'gatsby',
        'express', 'fastapi', 'django', 'flask', 'spring', 'laravel', 'rails',

        # Mobile frameworks
        'flutter', 'react native', 'ionic', 'xamarin',

        # Testing frameworks
        'pytest', 'unittest', 'jest', 'mocha', 'cypress', 'selenium',

        # Build tools
        'webpack', 'vite', 'rollup', 'parcel', 'grunt', 'gulp',
        'maven', 'gradle', 'cmake', 'make',

        # Databases
        'postgres', 'mysql', 'mongodb', 'redis', 'sqlite',

        # Cloud services
        'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'terraform',

        # Version control
        'git', 'github', 'gitlab', 'bitbucket',

        # Other tools
        'nginx', 'apache', 'elasticsearch', 'kafka', 'rabbitmq'
    }

    request_lower = request_text.lower()
    detected_tools = []

    for tool in frameworks_tools:
        if tool in request_lower:
            detected_tools.append(tool)

    return detected_tools


def clean_request_text(text: str) -> str:
    """Clean and normalize request text."""
    # Remove extra whitespace
    cleaned = re.sub(r'\s+', ' ', text.strip())

    # Remove common filler words at the beginning
    filler_patterns = [
        r'^(please\s+)?',
        r'^(can\s+you\s+)?',
        r'^(could\s+you\s+)?',
        r'^(would\s+you\s+)?',
        r'^(help\s+me\s+)?',
        r'^(i\s+need\s+to\s+)?',
        r'^(i\s+want\s+to\s+)?'
    ]

    for pattern in filler_patterns:
        cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)

    return cleaned.strip()


def validate_file_path(file_path: str, base_directory: str) -> bool:
    """Validate that a file path is safe and within the base directory."""
    try:
        # Resolve absolute path
        abs_file_path = os.path.abspath(os.path.join(base_directory, file_path))
        abs_base_dir = os.path.abspath(base_directory)

        # Check if file is within base directory (prevent directory traversal)
        return abs_file_path.startswith(abs_base_dir)
    except Exception:
        return False


def format_file_size(size_bytes: int) -> str:
    """Format file size in human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def generate_session_id() -> str:
    """Generate a unique session ID."""
    import time
    import random
    import string

    timestamp = str(int(time.time()))
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"code-session-{timestamp}-{random_suffix}"


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """Truncate text to specified length with suffix."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def estimate_tokens(text: str) -> int:
    """Rough estimation of token count for text."""
    # Very rough estimation: ~4 characters per token
    return len(text) // 4


def safe_file_name(name: str) -> str:
    """Convert string to safe filename."""
    # Remove or replace unsafe characters
    safe = re.sub(r'[<>:"/\\|?*]', '_', name)
    # Remove leading/trailing whitespace and periods
    safe = safe.strip('. ')
    # Limit length
    if len(safe) > 100:
        safe = safe[:100]
    return safe or 'unnamed'


def parse_key_value_options(options_text: str) -> Dict[str, str]:
    """Parse key=value options from text."""
    options = {}
    # Pattern to match key=value pairs
    pattern = r'(\w+)=(["\']?)([^"\'\s]+)\2'
    matches = re.findall(pattern, options_text)

    for key, quote, value in matches:
        options[key] = value

    return options


def format_duration(seconds: float) -> str:
    """Format duration in human-readable format."""
    if seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.1f}m"
    else:
        hours = seconds / 3600
        return f"{hours:.1f}h"