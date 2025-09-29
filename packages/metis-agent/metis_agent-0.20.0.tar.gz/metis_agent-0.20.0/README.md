# Metis Agent

[![PyPI version](https://badge.fury.io/py/metis-agent.svg)](https://badge.fury.io/py/metis-agent)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue)](https://opensource.org/licenses/Apache-2.0)
[![Downloads](https://pepy.tech/badge/metis-agent)](https://pepy.tech/project/metis-agent)
[![Security](https://img.shields.io/badge/security-enterprise--grade-green.svg)](./SECURITY_IMPLEMENTATION.md)

A powerful, modular framework for building AI agents with intelligent memory management and minimal boilerplate code. Metis Agent provides a comprehensive toolkit for creating intelligent agents that can understand user queries, plan and execute complex tasks, and maintain persistent conversations.

**Latest Release: v0.6.0** - Major expansion with secure code execution, advanced tools, and enterprise-grade capabilities.

### What's New in v0.6.0
- **🔒 E2B Code Sandbox** - Secure Python code execution in isolated cloud environments
- **🛠️ 36+ Advanced Tools** - Comprehensive toolkit for development, research, and analysis
- **🔧 Smart Orchestrator** - Intelligent tool selection with parameter extraction
- **📊 Enhanced Analytics** - Advanced memory management with Titans-inspired system
- **🌐 Enterprise Ready** - MCP integration, blueprint system, and production APIs
- **⚡ Performance Optimized** - Improved query analysis and execution strategies
- **🎯 Developer Focused** - Git integration, project management, and automated workflows

## Features

### 🏢 **Core Architecture**
- **Smart Orchestrator**: Intelligent tool selection with parameter extraction and execution strategies
- **Enhanced Memory System**: Titans-inspired adaptive memory with token-aware context management
- **Query Analyzer**: LLM-powered complexity analysis for optimal tool routing
- **Session Management**: Persistent conversations with automatic context preservation

### 🤖 **LLM Integration**
- **Multiple Providers**: OpenAI, Groq, Anthropic, HuggingFace with seamless switching
- **Model Flexibility**: Support for GPT-4, Claude, Llama, Mixtral, and custom models
- **Secure Authentication**: Encrypted API key management with environment fallback

### 🛠️ **Advanced Tool Suite (36+ Tools)**

#### **🔒 Security & Execution**
- **E2B Code Sandbox**: Secure Python execution in isolated cloud environments
- **Bash Tool**: Safe system command execution with output capture

#### **💻 Development Tools**
- **Git Integration**: Complete workflow management (clone, commit, push, merge, etc.)
- **Code Generation**: Multi-language code creation with best practices
- **Unit Test Generator**: Automated test creation with comprehensive coverage
- **Dependency Analyzer**: Project dependency analysis and optimization
- **Project Management**: Full lifecycle management with validation

#### **🔍 Research & Analysis**
- **Deep Research**: Multi-source research with citation management
- **Data Analysis**: Advanced analytics with pandas, numpy, visualization
- **Web Scraper**: Intelligent content extraction with Firecrawl integration
- **Google Search**: Real-time web search with result processing

#### **📝 Content & Communication**
- **Content Generation**: Multi-format content creation (blogs, docs, emails)
- **Text Analyzer**: Advanced NLP analysis with sentiment and entity recognition
- **Blueprint Execution**: Automated workflow and process execution

#### **📁 File & System Operations**
- **File Manager**: Complete file system operations with safety checks
- **Read/Write Tools**: Intelligent file handling with format detection
- **Grep Tool**: Advanced search with regex and pattern matching

### 🌐 **Enterprise Features**
- **MCP Integration**: Model Context Protocol server support
- **Blueprint System**: Workflow automation and process management
- **CLI Interface**: Comprehensive command-line tools for all operations
- **Web API**: RESTful endpoints for integration and automation
- **Memory Analytics**: Real-time performance monitoring and insights
- **Tool Registry**: Dynamic tool discovery and registration system

## Installation

```bash
pip install metis-agent
```

## Starter Templates

Get started quickly with our comprehensive collection of templates and examples:

**[Metis Agent Starter Templates](https://github.com/metis-analytics/metis-starter)** - A complete collection of templates for different use cases:

- **Basic Agent Template** - Simple agent for beginners and quick prototypes
- **Custom Agent Template** - Specialized agents with custom personalities
- **Web App Template** - Flask-based web chat interface
- **Advanced Integration Template** - Enterprise multi-agent systems
- **Custom Tools Template** - Examples for extending agent capabilities
- **Simple Custom Tool Example** - Step-by-step tool development guide

```bash
# Clone the starter templates
git clone https://github.com/metis-analytics/metis-starter.git
cd metis-starter

# Run your first agent
python templates/basic_agent_template.py
```

Each template includes:
- Complete working examples
- Detailed documentation
- Setup instructions
- Customization guides
- Best practices

## Quick Start

### Basic Usage

```python
from metis_agent import SingleAgent

# Create an agent
agent = SingleAgent()

# Process a query
response = agent.process_query("Write a Python function to calculate Fibonacci numbers")
print(response)
```

### Using Different LLM Providers

```python
from metis_agent import SingleAgent, configure_llm

# Configure LLM (OpenAI, Groq, Anthropic, or HuggingFace)
configure_llm("groq", "llama-3.1-8b-instant", "your-api-key")

# Create an agent
agent = SingleAgent()

# Process a query
response = agent.process_query("Explain quantum computing in simple terms")
print(response)
```

### Secure Code Execution with E2B

```python
from metis_agent import SingleAgent

# Create an agent (E2B tool auto-detected)
agent = SingleAgent()

# Execute Python code securely in cloud sandbox
response = agent.process_query("""
Execute this Python code:
```python
import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]}
df = pd.DataFrame(data)

# Create visualization
plt.figure(figsize=(8, 6))
plt.plot(df['x'], df['y'], marker='o')
plt.title('Sample Data Visualization')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()

print(f"Data shape: {df.shape}")
print(df.describe())
```
""")

print(response)
```

### Creating Custom Tools

```python
from metis_agent import SingleAgent, BaseTool, register_tool

class MyCustomTool(BaseTool):
    name = "custom_tool"
    description = "A custom tool for specialized tasks"
    
    def can_handle(self, task):
        return "custom task" in task.lower()
        
    def execute(self, task):
        return f"Executed custom tool on: {task}"

# Register the tool
register_tool("custom_tool", MyCustomTool)

# Create an agent
agent = SingleAgent()

# Process a query
response = agent.process_query("Perform a custom task")
print(response)
```

### Using Titans Memory

```python
from metis_agent import SingleAgent

# Create an agent with Titans memory
agent = SingleAgent(use_titans_memory=True)

# Process queries with memory
result1 = agent.process_query("What is machine learning?", session_id="user123")
result2 = agent.process_query("How does it relate to AI?", session_id="user123")
```

## Command Line Interface

Metis Agent provides a comprehensive command-line interface for all operations:

### Core Commands

```bash
# Interactive chat mode
metis chat

# Run a single query
metis run "Write a Python function to calculate Fibonacci numbers"

# Run with specific LLM provider
metis run "Explain quantum computing" --llm groq --model llama-3.1-8b-instant

# Run with memory enabled
metis run "What did we discuss earlier?" --memory --session-id user123
```

### Agent Management

```bash
# Create a new agent configuration
metis agent create --name "CodeExpert" --personality "Expert programming assistant"

# List all configured agents
metis agent list

# Use a specific agent
metis run "Help me debug this code" --agent CodeExpert

# Delete an agent
metis agent delete CodeExpert
```

### API Key Management

```bash
# Set API keys for different providers
metis auth set-key openai sk-your-openai-key
metis auth set-key groq gsk_your-groq-key
metis auth set-key anthropic your-anthropic-key
metis auth set-key e2b your-e2b-api-key

# List configured API keys (shows providers only, not keys)
metis auth list-keys

# Remove an API key
metis auth remove-key openai

# Test API key connectivity
metis auth test openai

# View security information
metis security-info
```

## 🔒 Enterprise Security

Metis Agent implements **enterprise-grade security** with multiple layers of protection:

### Security Features

- **🔐 AES-256-GCM Encryption** - API keys encrypted with military-grade encryption
- **🛡️ Input Validation** - Multi-layer protection against injection attacks
- **🚫 Command Injection Prevention** - Whitelist-only command execution
- **📂 Path Traversal Protection** - Prevents unauthorized file system access
- **📝 Comprehensive Audit Logging** - All security events tracked
- **🔄 Key Rotation** - Built-in encryption key rotation capabilities

### Quick Security Check

```bash
# Check security status
metis security-info

# Rotate encryption keys (recommended monthly)
metis auth rotate-keys
```

**📖 Complete Security Documentation**: [SECURITY_IMPLEMENTATION.md](./SECURITY_IMPLEMENTATION.md)  
**⚡ Security Installation Guide**: [SECURITY_INSTALLATION.md](./SECURITY_INSTALLATION.md)

### E2B Code Sandbox Setup

```bash
# Set E2B API key for secure code execution
metis auth set-key e2b your-e2b-api-key

# Test E2B connectivity
metis auth test e2b

# Execute code in sandbox via CLI
metis chat "Execute this Python code: print('Hello from E2B sandbox!')"
```

### Tool Management

```bash
# List all available tools
metis tools list

# Get detailed information about a tool
metis tools info CodeGenerationTool

# Test a specific tool
metis tools test CodeGenerationTool "Write a hello world function"

# Enable/disable tools
metis tools enable GoogleSearchTool
metis tools disable FirecrawlTool
```

### Memory Operations

```bash
# Show memory statistics
metis memory stats

# Clear memory for a session
metis memory clear --session-id user123

# Export memory to file
metis memory export --output memory_backup.json

# Import memory from file
metis memory import --input memory_backup.json

# Search memory contents
metis memory search "machine learning"
```

### Web Server

```bash
# Start web server with default settings
metis serve

# Start with custom port and memory enabled
metis serve --port 8080 --memory --cors

# Start with specific agent
metis serve --agent CodeExpert --port 5000

# Start with authentication
metis serve --auth --api-key your-server-api-key
```

### Configuration

```bash
# Configure default LLM provider
metis config set-llm --provider groq --model llama-3.1-8b-instant

# Set default memory settings
metis config set-memory --type titans --path ./memory

# View current configuration
metis config show

# Reset configuration to defaults
metis config reset
```


### Development Tools

```bash
# Run system diagnostics
metis dev diagnose

# Test all components
metis dev test

# Generate development templates
metis dev template --type custom-tool --name MyTool

# Profile agent performance
metis dev profile "Complex query for performance testing"
```

## Web Server

Metis Agent includes a web server for API access:

```bash
# Start the web server
metis serve
```

Then make requests to the API:

```bash
curl -X POST http://localhost:5000/api/query \
  -H "Content-Type: application/json" \
  -d '{"query": "Write a Python function to calculate Fibonacci numbers"}'
```

API Endpoints:

- `GET /` - Server status
- `POST /api/query` - Process a query
- `GET /api/agent-identity` - Get agent information
- `GET /api/memory-insights` - Get memory statistics
- `GET /api/tools` - List available tools

## Detailed Documentation

### Core Components

#### SingleAgent

The main agent class that orchestrates all components:

```python
from metis_agent import SingleAgent

agent = SingleAgent(
    use_titans_memory=False,  # Enable/disable Titans memory
    tools=None,               # Custom tools (uses all available if None)
    llm_provider="openai",    # LLM provider
    llm_model=None,           # LLM model (uses default if None)
    memory_path=None,         # Path to memory database
    task_file=None            # Path to task file
)
```

#### Intent Router

Determines whether a user query is a question or a task:

```python
from metis_agent.core.intent_router import IntentRouter

router = IntentRouter()
intent = router.classify("What is the capital of France?")  # Returns "question"
intent = router.classify("Create a Python script to sort a list")  # Returns "task"
```

#### Task Manager

Manages tasks and their status:

```python
from metis_agent.core.task_manager import TaskManager

task_manager = TaskManager()
task_manager.add_task("Write a function to calculate Fibonacci numbers")
task_manager.mark_complete("Write a function to calculate Fibonacci numbers")
tasks = task_manager.get_all_tasks()
```

#### Memory Systems

SQLite-based memory:

```python
from metis_agent.memory.sqlite_store import SQLiteMemory

memory = SQLiteMemory("memory.db")
memory.store_input("user123", "What is machine learning?")
memory.store_output("user123", "Machine learning is...")
context = memory.get_context("user123")
```

Titans-inspired adaptive memory:

```python
from metis_agent.memory.titans.titans_memory import TitansInspiredMemory

memory = TitansInspiredMemory("memory_dir")
memory.store_memory("Machine learning is...", "ai_concepts")
relevant_memories = memory.retrieve_relevant_memories("What is deep learning?")
```

### LLM Providers

Configure and use different LLM providers:

```python
from metis_agent.core.llm_interface import configure_llm, get_llm

# Configure LLM
configure_llm("openai", "gpt-4o")  # OpenAI
configure_llm("groq", "llama-3.1-8b-instant")  # Groq
configure_llm("anthropic", "claude-3-opus-20240229")  # Anthropic
configure_llm("huggingface", "mistralai/Mixtral-8x7B-Instruct-v0.1")  # HuggingFace

# Get configured LLM
llm = get_llm()
response = llm.chat([{"role": "user", "content": "Hello!"}])
```

### Tools

Available tools (36+ advanced tools):

#### **Security & Execution**
- `E2BCodeSandboxTool`: Secure Python code execution in isolated cloud environments
- `BashTool`: Safe system command execution with output capture

#### **Development & Code**
- `GitIntegrationTool`: Complete Git workflow management
- `CodeGenerationTool`: Multi-language code generation with best practices
- `PythonCodeTool`: Python-specific code analysis and execution
- `UnitTestGeneratorTool`: Automated test creation with comprehensive coverage
- `DependencyAnalyzerTool`: Project dependency analysis and optimization
- `EditTool`: Intelligent code editing with context awareness

#### **Research & Analysis**
- `DeepResearchTool`: Multi-source research with citation management
- `DataAnalysisTool`: Advanced analytics with pandas, numpy, visualization
- `GoogleSearchTool`: Real-time web search with result processing
- `WebScraperTool`: Intelligent content extraction
- `FirecrawlTool`: Advanced web scraping and content analysis
- `TextAnalyzerTool`: NLP analysis with sentiment and entity recognition

#### **Content & Communication**
- `ContentGenerationTool`: Multi-format content creation (blogs, docs, emails)
- `ConversationManagerTool`: Advanced dialogue management

#### **Project & Workflow Management**
- `ProjectManagementTool`: Full project lifecycle management
- `ProjectValidationTool`: Automated project validation and quality checks
- `BlueprintExecutionTool`: Workflow automation and process execution
- `RequirementsAnalysisTool`: Automated requirements gathering and analysis
- `ToolGeneratorTool`: Dynamic tool creation and customization

#### **File & System Operations**
- `FileManagerTool`: Complete file system operations with safety checks
- `FilesystemTool`: Advanced file system navigation and management
- `ReadTool`: Intelligent file reading with format detection
- `WriteTool`: Smart file writing with backup and validation
- `GrepTool`: Advanced search with regex and pattern matching

#### **Mathematical & Scientific**
- `AdvancedMathTool`: Complex mathematical computations and analysis
- `CalculatorTool`: Mathematical calculations with expression parsing

Creating custom tools:

```python
from metis_agent.tools.base import BaseTool
from metis_agent.tools.registry import register_tool

class MyTool(BaseTool):
    name = "my_tool"
    description = "Custom tool for specific tasks"
    
    def can_handle(self, task):
        # Determine if this tool can handle the task
        return "specific task" in task.lower()
        
    def execute(self, task):
        # Execute the task
        return f"Task executed: {task}"

# Register the tool
register_tool("my_tool", MyTool)
```

### API Key Management

Secure storage and retrieval of API keys:

```python
from metis_agent.auth.api_key_manager import APIKeyManager

key_manager = APIKeyManager()
key_manager.set_key("openai", "your-api-key")
api_key = key_manager.get_key("openai")
services = key_manager.list_services()
```

## Testing

Run the comprehensive test suite:

```bash
# Run system tests
python metis_agent/test_system.py

# Run CLI tests
python metis_agent/test_cli.py
```

## Advanced Usage

### Session Management

Maintain context across multiple interactions:

```python
agent = SingleAgent()

# First query
response1 = agent.process_query(
    "What are the main types of machine learning?",
    session_id="user123"
)

# Follow-up query (uses context from first query)
response2 = agent.process_query(
    "Can you explain supervised learning in more detail?",
    session_id="user123"
)
```

### Tool Selection

Specify which tool to use for a query:

```python
agent = SingleAgent()

# Use a specific tool
response = agent.process_query(
    "Generate a Python function to sort a list",
    tool_name="CodeGenerationTool"
)
```

### Memory Insights

Get insights about the agent's memory:

```python
agent = SingleAgent(use_titans_memory=True)

# Process some queries
agent.process_query("What is machine learning?", session_id="user123")
agent.process_query("Explain neural networks", session_id="user123")

# Get memory insights
insights = agent.get_memory_insights()
print(insights)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contact & Links

- **PyPI Package**: [https://pypi.org/project/metis-agent/](https://pypi.org/project/metis-agent/)
- **Starter Templates**: [https://github.com/metis-analytics/metis-starter](https://github.com/metis-analytics/metis-starter)
- **Documentation**: [https://github.com/metis-analytics/metis-agent/wiki](https://github.com/metis-analytics/metis-agent/wiki)
- **Issues & Support**: [https://github.com/metis-analytics/metis-agent/issues](https://github.com/metis-analytics/metis-agent/issues)
- **Discussions**: [https://github.com/metis-analytics/metis-agent/discussions](https://github.com/metis-analytics/metis-agent/discussions)

---

<p align="center">
  <strong>Metis Agent - Building Intelligent AI Systems</strong>
</p>