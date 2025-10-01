# xlibrary

A comprehensive Python library ecosystem with modular "pillars" that provide specialized functionality for modern development needs.

## Overview

xlibrary is designed with a pillar-based architecture where each pillar is independently installable and has its own dependencies. This allows you to install only the functionality you need while maintaining a clean, modular codebase.

## Available Pillars

### 🤖 AI Pillar
Multi-provider AI abstraction layer supporting:
- **Claude** (Anthropic)
- **OpenAI** (GPT models)
- **DeepSeek**
- **Mock Provider** (for testing)

Features: conversation management, metrics, health monitoring, rate limiting, structured logging.

### ⚙️ Config Pillar
Configuration management with:
- TOML support with interpolation
- Environment variable integration
- Encrypted configuration values
- Schema validation

### 📥 Download Pillar
Advanced download manager supporting:
- Multi-content downloads
- Progress tracking
- Resume capability
- Rich terminal output
- Async operations

### 🎬 Media Pillar
Media processing capabilities:
- Video processing with MoviePy
- Image processing with Pillow
- Watermarking engine
- Animation support
- OpenCV integration

### 🔒 Encryption Pillar
Security and encryption utilities:
- Modern cryptographic operations
- Secure key management
- Data encryption/decryption

### 📁 Files Pillar
File and directory management:
- Advanced file operations
- Magic number detection
- Compression utilities
- Deduplication

### 📦 Imports Pillar
File import management system:
- Pattern matching
- File watching
- Import processing
- Type detection

### 🔄 Pipeline Pillar
Universal pipeline management:
- Data processing pipelines
- Stage management
- Error handling
- Progress tracking

### 💻 CLI Pillar
Professional command-line interface framework:
- Rich terminal output
- Interactive menus
- Progress indicators
- Keyboard navigation

### 📡 Communication Pillar
Communication utilities:
- Email integration
- Message handling
- Provider abstraction

## Installation

### Install Specific Pillars
```bash
# Install just the AI pillar
pip install xlibrary[ai]

# Install configuration management
pip install xlibrary[config]

# Install media processing
pip install xlibrary[media]

# Install download manager
pip install xlibrary[download]
```

### Install Multiple Pillars
```bash
# Install AI and config pillars
pip install xlibrary[ai,config]

# Install all pillars
pip install xlibrary[all]
```

### Development Installation
```bash
pip install xlibrary[dev]
```

## Quick Start

### AI Pillar Example
```python
from xlibrary.ai import AIManager

# Initialize with your preferred provider
ai = AIManager(provider="claude", api_key="your-api-key")

# Simple request
response = ai.request("Hello, how are you?")
print(response.content)

# Streaming response
for chunk in ai.stream("Tell me a story"):
    print(chunk.content, end="")
```

### Config Pillar Example
```python
from xlibrary.config import ConfigManager

# Load and manage configuration
config = ConfigManager("config.toml")
database_url = config.get("database.url")
api_key = config.get("api.key", encrypted=True)
```

### Download Pillar Example
```python
from xlibrary.download import DownloadManager

# Download with progress tracking
downloader = DownloadManager()
result = downloader.download(
    "https://example.com/file.zip",
    destination="./downloads/"
)
```

## Features

- **Modular Architecture**: Install only what you need
- **Type Safety**: Comprehensive type hints throughout
- **Async Support**: Built-in async operations where applicable
- **Rich Logging**: Structured logging with configurable levels
- **Testing**: Comprehensive test suite with 95%+ coverage
- **Documentation**: Extensive documentation and examples

## Requirements

- Python 3.8+
- Individual pillar dependencies as needed

## Development

### Building
```bash
./scripts/build.sh
```

### Testing
```bash
pytest
```

### Code Quality
```bash
black src/ tests/     # Format code
mypy src/xlibrary     # Type checking
flake8 src/ tests/    # Linting
```

## Project Structure

```
xlibrary/
├── src/xlibrary/          # Main package
│   ├── ai/               # AI pillar
│   ├── config/           # Config pillar
│   ├── download/         # Download pillar
│   ├── media/            # Media pillar
│   ├── encryption/       # Encryption pillar
│   ├── files/            # Files pillar
│   ├── imports/          # Imports pillar
│   ├── pipeline/         # Pipeline pillar
│   ├── cli/              # CLI pillar
│   └── communication/    # Communication pillar
├── tests/                # Test suite
├── scripts/              # Build and utility scripts
└── pyproject.toml        # Project configuration
```

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please ensure:
1. Tests pass: `pytest`
2. Code is formatted: `black src/ tests/`
3. Types are checked: `mypy src/xlibrary`
4. Linting passes: `flake8 src/ tests/`

## Support

- Documentation: [GitHub Repository](https://github.com/xlibrary/xlibrary)
- Issues: [GitHub Issues](https://github.com/xlibrary/xlibrary/issues)
- Repository: [GitHub](https://github.com/xlibrary/xlibrary)