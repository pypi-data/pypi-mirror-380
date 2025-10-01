# url-is-in

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

A Python package for efficiently checking if URLs are part of large whitelists or blacklists. Built for speed and scalability, `url-is-in` provides different matching algorithms based on dataset size and provides both URL and SURT-based matching capabilities.

## Features

- 🌐 **URL Normalization**: Uses SURT (Sort-friendly URI Reordering Transform) for consistent URL comparison
- 🔍 **Subdomain Matching**: Optional subdomain matching for domain-based filtering
- 📊 **Scalable**: Efficiently handles large URL lists using Trie matching (tested with > 1M of URLs)
- 🎯 **Flexible**: Support for both URL and SURT-based matching
- 🐍 **Python 3.8+**: Modern Python support with type hints

## Installation

### Using pip

```bash
pip install url-is-in
```

### Using uv (recommended for development)

```bash
uv add url-is-in
```

### From source

```bash
git clone https://github.com/commoncrawl/url-is-in.git
cd url-is-in
pip install -e .
```

## Requirements

- **Python**: 3.8 or higher
- **Dependencies**:
  - `surt` - For URL normalization and SURT conversion

## Quick Start

### Basic URL Matching

```python
from url_is_in import URLMatcher

# Create a matcher with a list of URLs
urls = [
    'https://example.com',
    'https://test.org/specific/path',
    'https://github.com/user/repo'
]

matcher = URLMatcher(urls)

# Check if URLs match
print(matcher.is_in('https://example.com/any/path'))  # True
print(matcher.is_in('https://test.org/specific/path/file.html'))  # True
print(matcher.is_in('https://other.com'))  # False
```

### Subdomain Matching

```python
from url_is_in import URLMatcher

# Enable subdomain matching (default: True)
matcher = URLMatcher(['https://example.com'], match_subdomains=True)

print(matcher.is_in('https://www.example.com'))      # True
print(matcher.is_in('https://api.example.com'))      # True
print(matcher.is_in('https://sub.example.com/path')) # True
```

### SURT-based Matching

For advanced use cases, you can work directly with SURT strings:

```python
from url_is_in import SURTMatcher

# Work with SURT strings directly
surts = [
    'com,example)/',
    'org,test)/specific/path',
    'com,github)/user/repo'
]

matcher = SURTMatcher(surts)

# Check SURT strings
print(matcher.is_in('com,example)/any/path'))  # True
print(matcher.is_in('org,test)/other'))        # False
```

### Algorithm Selection

The package automatically selects the optimal matching algorithm:

```python
from url_is_in import URLMatcher

# Automatic selection (default)
matcher = URLMatcher(urls, mode="auto")  # Trie for >100 URLs, tuple for ≤100

# Manual selection
fast_matcher = URLMatcher(urls, mode="trie")    # Always use trie
simple_matcher = URLMatcher(urls, mode="tuple") # Always use tuple
```


### Setting up development environment

```bash
# Clone the repository
git clone https://github.com/commoncrawl/url-is-in.git
cd url-is-in

# Install with development dependencies
uv sync --extra dev

# Run tests
pytest

# Run linting
ruff check .
ruff format .
```

### Running tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-fail-under=95
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
