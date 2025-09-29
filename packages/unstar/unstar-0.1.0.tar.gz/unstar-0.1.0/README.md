# unstar

A simple Python package to automate the removal of GitHub stars from your account.

## Features

- Remove all starred repositories from your GitHub account
- Built with modern Python packaging using `uv`
- Command-line interface for easy usage
- Rate limiting to respect GitHub API limits

## Installation

### From PyPI (recommended)

```bash
# Install using uv (recommended)
uv tool install unstar

# Or install using pip
pip install unstar
```

### From Source

```bash
git clone https://github.com/forkdo/unstar
cd unstar

uv sync
# or if you have `uv` installed globally
uv tool install -e 
```

## Usage

### Command Line Interface

After installation, you can use the `unstar` command:

```bash
unstar <your_github_access_token>
```

### Getting a GitHub Access Token

1. Go to [GitHub Settings > Personal Access Tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Select the following scopes:
   - `public_repo` (to access public repositories)
   - `user` (to access starred repositories)
4. Copy the generated token

### Example

```bash
unstar ghp_your_token_here
```

## Development

This project uses `uv` for dependency management and packaging.

### Setup Development Environment

```bash
git clone https://github.com/forkdo/unstar
cd unstar
uv sync
```

### Running from Source

```bash
uv run unstar <access_token>
# or
uv run python -m unstar.main <access_token>
```

### Building the Package

```bash
uv build
```

### Publishing to PyPI

```bash
# Build the package
uv build

# Publish to PyPI (requires authentication)
uv publish
```

## Requirements

- Python 3.8+
- `requests` library
- Valid GitHub personal access token

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests (if available)
5. Submit a pull request

## Disclaimer

Use this tool responsibly. Make sure you really want to unstar all your repositories before running it, as this action cannot be easily undone.
