"""
Project detection and management functionality.

This module handles project structure detection, analysis, and management
for various programming languages and frameworks.
"""

import os
import json
import glob
from pathlib import Path
from typing import Dict, List, Optional, Any, Set
import subprocess
import re

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False


class ProjectManager:
    """Manages project detection, analysis, and operations."""

    def __init__(self):
        self.console = Console() if RICH_AVAILABLE else None
        self.project_indicators = {
            'python': ['requirements.txt', 'setup.py', 'pyproject.toml', 'Pipfile', 'poetry.lock'],
            'javascript': ['package.json', 'yarn.lock', 'package-lock.json'],
            'typescript': ['tsconfig.json', 'package.json'],
            'java': ['pom.xml', 'build.gradle', 'gradle.properties'],
            'rust': ['Cargo.toml', 'Cargo.lock'],
            'go': ['go.mod', 'go.sum'],
            'php': ['composer.json', 'composer.lock'],
            'ruby': ['Gemfile', 'Gemfile.lock'],
            'csharp': ['*.csproj', '*.sln', 'packages.config'],
            'cpp': ['CMakeLists.txt', 'Makefile', 'conanfile.txt'],
            'swift': ['Package.swift', '*.xcodeproj'],
            'kotlin': ['build.gradle.kts', 'pom.xml'],
            'scala': ['build.sbt', 'project/'],
            'dart': ['pubspec.yaml', 'pubspec.lock'],
            'r': ['DESCRIPTION', 'renv.lock'],
            'julia': ['Project.toml', 'Manifest.toml']
        }

    def detect_project_context(self, directory: str, target_file: Optional[str] = None,
                             context_files: Optional[List[str]] = None) -> Dict[str, Any]:
        """Detect comprehensive project context."""
        context = {
            'directory': directory,
            'exists': os.path.exists(directory),
            'is_git_repo': self._is_git_repository(directory),
            'languages': [],
            'frameworks': [],
            'structure': {},
            'dependencies': {},
            'configuration': {},
            'target_file': target_file,
            'context_files': context_files or []
        }

        if not context['exists']:
            return context

        # Detect project type and languages
        context['languages'] = self._detect_languages(directory)
        context['frameworks'] = self._detect_frameworks(directory)

        # Analyze project structure
        context['structure'] = self._analyze_structure(directory)

        # Parse dependencies
        context['dependencies'] = self._parse_dependencies(directory, context['languages'])

        # Load configuration files
        context['configuration'] = self._load_configurations(directory)

        # Add file-specific context
        if target_file:
            context['file_context'] = self._analyze_file_context(target_file, directory)

        return context

    def _detect_languages(self, directory: str) -> List[str]:
        """Detect programming languages used in the project."""
        detected_languages = []

        for language, indicators in self.project_indicators.items():
            for indicator in indicators:
                if '*' in indicator:
                    # Glob pattern
                    if glob.glob(os.path.join(directory, indicator)):
                        detected_languages.append(language)
                        break
                else:
                    # Exact file match
                    if os.path.exists(os.path.join(directory, indicator)):
                        detected_languages.append(language)
                        break

        # Also detect by file extensions
        extension_map = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.java': 'java',
            '.rs': 'rust',
            '.go': 'go',
            '.php': 'php',
            '.rb': 'ruby',
            '.cs': 'csharp',
            '.cpp': 'cpp',
            '.cc': 'cpp',
            '.cxx': 'cpp',
            '.swift': 'swift',
            '.kt': 'kotlin',
            '.scala': 'scala',
            '.dart': 'dart',
            '.r': 'r',
            '.jl': 'julia'
        }

        for root, dirs, files in os.walk(directory):
            # Skip hidden directories and common build directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', 'target', 'build', 'dist']]

            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in extension_map:
                    lang = extension_map[ext]
                    if lang not in detected_languages:
                        detected_languages.append(lang)

        return detected_languages

    def _detect_frameworks(self, directory: str) -> List[str]:
        """Detect frameworks and libraries used."""
        frameworks = []

        # Framework detection patterns
        framework_patterns = {
            'react': ['package.json', r'"react"'],
            'vue': ['package.json', r'"vue"'],
            'angular': ['package.json', r'"@angular'],
            'express': ['package.json', r'"express"'],
            'fastapi': ['requirements.txt', r'fastapi'],
            'django': ['requirements.txt', r'[Dd]jango'],
            'flask': ['requirements.txt', r'[Ff]lask'],
            'spring': ['pom.xml', r'spring'],
            'laravel': ['composer.json', r'laravel'],
            'rails': ['Gemfile', r'rails'],
            'nextjs': ['package.json', r'"next"'],
            'nuxtjs': ['package.json', r'"nuxt"'],
            'svelte': ['package.json', r'"svelte"'],
            'gatsby': ['package.json', r'"gatsby"']
        }

        for framework, (file_pattern, content_pattern) in framework_patterns.items():
            file_path = os.path.join(directory, file_pattern)
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if re.search(content_pattern, content, re.IGNORECASE):
                            frameworks.append(framework)
                except Exception:
                    pass

        return frameworks

    def _analyze_structure(self, directory: str) -> Dict[str, Any]:
        """Analyze project directory structure."""
        structure = {
            'total_files': 0,
            'directories': [],
            'file_types': {},
            'size_bytes': 0,
            'main_files': []
        }

        important_files = [
            'README.md', 'README.rst', 'README.txt',
            'LICENSE', 'LICENSE.txt', 'LICENSE.md',
            'CHANGELOG.md', 'CHANGELOG.txt',
            'setup.py', 'setup.cfg', 'pyproject.toml',
            'package.json', 'tsconfig.json',
            'Makefile', 'CMakeLists.txt',
            'Dockerfile', 'docker-compose.yml'
        ]

        for root, dirs, files in os.walk(directory):
            # Skip hidden and build directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in [
                'node_modules', 'target', 'build', 'dist', '__pycache__', '.git'
            ]]

            rel_root = os.path.relpath(root, directory)
            if rel_root != '.':
                structure['directories'].append(rel_root)

            for file in files:
                if file.startswith('.'):
                    continue

                structure['total_files'] += 1
                file_path = os.path.join(root, file)

                # Track file types
                ext = os.path.splitext(file)[1].lower()
                if ext:
                    structure['file_types'][ext] = structure['file_types'].get(ext, 0) + 1

                # Track important files
                if file in important_files:
                    structure['main_files'].append(os.path.relpath(file_path, directory))

                # Calculate size
                try:
                    structure['size_bytes'] += os.path.getsize(file_path)
                except OSError:
                    pass

        return structure

    def _parse_dependencies(self, directory: str, languages: List[str]) -> Dict[str, List[str]]:
        """Parse project dependencies."""
        dependencies = {}

        # Python dependencies
        if 'python' in languages:
            dependencies['python'] = self._parse_python_dependencies(directory)

        # JavaScript/Node.js dependencies
        if 'javascript' in languages or 'typescript' in languages:
            dependencies['npm'] = self._parse_npm_dependencies(directory)

        # Add other language dependency parsing as needed

        return dependencies

    def _parse_python_dependencies(self, directory: str) -> List[str]:
        """Parse Python dependencies from various files."""
        deps = []

        # requirements.txt
        req_file = os.path.join(directory, 'requirements.txt')
        if os.path.exists(req_file):
            deps.extend(self._parse_requirements_txt(req_file))

        # setup.py
        setup_file = os.path.join(directory, 'setup.py')
        if os.path.exists(setup_file):
            deps.extend(self._parse_setup_py(setup_file))

        # pyproject.toml
        pyproject_file = os.path.join(directory, 'pyproject.toml')
        if os.path.exists(pyproject_file):
            deps.extend(self._parse_pyproject_toml(pyproject_file))

        return list(set(deps))  # Remove duplicates

    def _parse_npm_dependencies(self, directory: str) -> List[str]:
        """Parse npm dependencies from package.json."""
        package_file = os.path.join(directory, 'package.json')
        if not os.path.exists(package_file):
            return []

        try:
            with open(package_file, 'r', encoding='utf-8') as f:
                package_data = json.load(f)

            deps = []
            for dep_type in ['dependencies', 'devDependencies', 'peerDependencies']:
                if dep_type in package_data:
                    deps.extend(package_data[dep_type].keys())

            return deps
        except Exception:
            return []

    def _parse_requirements_txt(self, file_path: str) -> List[str]:
        """Parse requirements.txt file."""
        deps = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        # Extract package name (before version specifiers)
                        dep = re.split(r'[>=<!]', line)[0].strip()
                        if dep:
                            deps.append(dep)
        except Exception:
            pass
        return deps

    def _parse_setup_py(self, file_path: str) -> List[str]:
        """Parse setup.py for dependencies."""
        deps = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Look for install_requires
            install_requires_match = re.search(
                r'install_requires\s*=\s*\[(.*?)\]',
                content,
                re.DOTALL
            )

            if install_requires_match:
                requires_content = install_requires_match.group(1)
                # Extract quoted dependencies
                dep_matches = re.findall(r'["\']([^"\'>=<!]+)', requires_content)
                deps.extend(dep_matches)

        except Exception:
            pass
        return deps

    def _parse_pyproject_toml(self, file_path: str) -> List[str]:
        """Parse pyproject.toml for dependencies."""
        deps = []
        try:
            import toml
            with open(file_path, 'r', encoding='utf-8') as f:
                data = toml.load(f)

            # Poetry dependencies
            if 'tool' in data and 'poetry' in data['tool']:
                poetry_deps = data['tool']['poetry'].get('dependencies', {})
                deps.extend([dep for dep in poetry_deps.keys() if dep != 'python'])

            # PEP 621 dependencies
            if 'project' in data:
                project_deps = data['project'].get('dependencies', [])
                for dep in project_deps:
                    dep_name = re.split(r'[>=<!]', dep)[0].strip()
                    if dep_name:
                        deps.append(dep_name)

        except ImportError:
            # toml library not available, try basic parsing
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Basic regex parsing for dependencies
                dep_matches = re.findall(r'["\']([a-zA-Z0-9-_]+)["\']', content)
                deps.extend(dep_matches)
            except Exception:
                pass
        except Exception:
            pass

        return deps

    def _load_configurations(self, directory: str) -> Dict[str, Any]:
        """Load various configuration files."""
        configs = {}

        config_files = {
            'package.json': self._load_json_config,
            'tsconfig.json': self._load_json_config,
            'pyproject.toml': self._load_toml_config,
            '.gitignore': self._load_text_config,
            'README.md': self._load_text_config,
            'Dockerfile': self._load_text_config
        }

        for config_file, loader in config_files.items():
            file_path = os.path.join(directory, config_file)
            if os.path.exists(file_path):
                configs[config_file] = loader(file_path)

        return configs

    def _load_json_config(self, file_path: str) -> Any:
        """Load JSON configuration file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return None

    def _load_toml_config(self, file_path: str) -> Any:
        """Load TOML configuration file."""
        try:
            import toml
            with open(file_path, 'r', encoding='utf-8') as f:
                return toml.load(f)
        except ImportError:
            return {"error": "toml library not available"}
        except Exception:
            return None

    def _load_text_config(self, file_path: str) -> str:
        """Load text configuration file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception:
            return ""

    def _analyze_file_context(self, file_path: str, project_dir: str) -> Dict[str, Any]:
        """Analyze specific file context."""
        if not os.path.isabs(file_path):
            file_path = os.path.join(project_dir, file_path)

        context = {
            'exists': os.path.exists(file_path),
            'relative_path': os.path.relpath(file_path, project_dir),
            'size_bytes': 0,
            'lines': 0,
            'extension': os.path.splitext(file_path)[1],
            'language': None,
            'content_preview': None
        }

        if context['exists']:
            try:
                # File stats
                stat = os.stat(file_path)
                context['size_bytes'] = stat.st_size

                # Content analysis
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    context['lines'] = len(content.splitlines())
                    context['content_preview'] = content[:500]  # First 500 chars

                # Language detection
                context['language'] = self._detect_file_language(file_path, content)

            except Exception as e:
                context['error'] = str(e)

        return context

    def _detect_file_language(self, file_path: str, content: str) -> Optional[str]:
        """Detect programming language of a file."""
        ext = os.path.splitext(file_path)[1].lower()

        extension_map = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.java': 'java',
            '.rs': 'rust',
            '.go': 'go',
            '.php': 'php',
            '.rb': 'ruby',
            '.cs': 'csharp',
            '.cpp': 'cpp',
            '.c': 'c',
            '.h': 'c',
            '.hpp': 'cpp',
            '.swift': 'swift',
            '.kt': 'kotlin',
            '.scala': 'scala',
            '.dart': 'dart',
            '.r': 'r',
            '.jl': 'julia',
            '.sh': 'bash',
            '.sql': 'sql',
            '.html': 'html',
            '.css': 'css',
            '.scss': 'scss',
            '.less': 'less',
            '.json': 'json',
            '.xml': 'xml',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.toml': 'toml',
            '.md': 'markdown',
            '.rst': 'rst'
        }

        return extension_map.get(ext)

    def _is_git_repository(self, directory: str) -> bool:
        """Check if directory is a git repository."""
        git_dir = os.path.join(directory, '.git')
        return os.path.exists(git_dir)

    def create_project(self, name: str, template: Optional[str] = None,
                      language: Optional[str] = None, framework: Optional[str] = None,
                      features: Optional[List[str]] = None):
        """Create a new project with specified parameters."""
        # Implementation for project creation
        pass

    def analyze_project(self, directory: str):
        """Analyze and display project information."""
        context = self.detect_project_context(directory)

        if RICH_AVAILABLE and self.console:
            self._display_analysis_rich(context)
        else:
            self._display_analysis_plain(context)

    def _display_analysis_rich(self, context: Dict[str, Any]):
        """Display project analysis with Rich formatting."""
        # Implementation for Rich display
        pass

    def _display_analysis_plain(self, context: Dict[str, Any]):
        """Display project analysis with plain text."""
        # Implementation for plain text display
        pass

    def show_status(self, directory: str):
        """Show current project status."""
        # Implementation for status display
        pass

    def show_detailed_status(self, directory: str):
        """Show detailed project status."""
        # Implementation for detailed status
        pass