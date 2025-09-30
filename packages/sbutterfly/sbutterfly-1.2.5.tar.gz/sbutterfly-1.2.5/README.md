# Butterfly

A lightweight, extensible social media management tool.

## Overview

Butterfly is a Python framework for managing posts across multiple social media platforms through a unified interface. It uses a plugin-based architecture to support different social media services.

Currently supported platforms:
- Twitter
- Mastodon
- BlueSky

## Installation

Requires Python 3.12+ & uv/pipx

```bash
uv tool install sbutterfly
```

## Usage

### Command Line Interface

```bash
# List available plugins
sbutterfly --list-plugins

# Validate credentials
sbutterfly --method validate

# Post a message
sbutterfly --plugins twitter --method execute --message "Hello from Butterfly!"
sbutterfly --plugins mastodon --method execute --message "Hello from Butterfly!"
sbutterfly --plugins bluesky --method execute --message "Hello from Butterfly!"
# or
sbutterfly --method execute --message "Hello from Butterfly!"
```

## Configuration

Butterfly uses environment variables for authentication:

### Environment Variables
```
TWITTER_CONSUMER_KEY
TWITTER_CONSUMER_SECRET
TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_TOKEN_SECRET
MASTODON_BEARER_TOKEN
BSKY_USERNAME
BSKY_PASSWORD
```

## Extending Butterfly

To create a new social media plugin:

1. Create a new file in the `plugins` directory
2. Implement a class that adheres to the Plugin protocol:
   - `get_name()`: Returns the plugin's name
   - `validate()`: Validates the plugin's credentials
   - `execute()`: Posts content to the social media platform

See `plugins/twitter.py` for an example implementation.

## Development
```bash
git clone https://github.com/danwald/butterfly.git
cd butterfly

# Install development dependencies
uv sync

# Run tests
make test

# Run linting
make lint
make type
```

### Using as a Library

```python
from plugins.twitter import Twitter

# Create a Twitter plugin instance
twitter = Twitter()

# Validate credentials
if twitter.validate():
    # Post a message
    twitter.execute("Hello from Butterfly!")
```

## Todo
- support meta threads
