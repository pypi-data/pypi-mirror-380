# Entangle Matrix SDK for Python

[![PyPI version](https://badge.fury.io/py/entangle-matrix.svg)](https://badge.fury.io/py/entangle-matrix)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python SDK for the Entangle Matrix API, enabling developers to easily integrate Matrix messaging capabilities into their applications. Send messages, share files, manage rooms, and more with a simple, async-first API.

## 🚀 Features

- **Async/Await Support**: Built with `aiohttp` for high-performance async operations
- **Type Safety**: Full type hints and data validation using dataclasses
- **File Upload Support**: Send images, audio, and files with automatic type detection
- **Room Management**: Create, join, and manage Matrix rooms programmatically
- **Error Handling**: Comprehensive exception hierarchy for robust error handling
- **Authentication**: Support for API key authentication
- **Validation**: Built-in validation for Matrix room IDs, file types, and sizes

## 📦 Installation

```bash
pip install entangle-matrix
```

### Development Installation

```bash
git clone https://github.com/qbit-codes/entangle-python-client.git
cd entangle-python-client
pip install -e .[dev]
```

## 🔧 Quick Start

### Basic Message Sending

```python
import asyncio
from entangle_matrix import EntangleMatrixClient

async def main():
    async with EntangleMatrixClient(
        base_url="http://localhost:8000",
        api_key="your-api-key"  # Optional
    ) as client:

        # Send a simple message
        message = await client.send_message(
            room_id="!roomid:example.com",
            message="Hello, Matrix! 👋"
        )

        print(f"Message sent! Event ID: {message.event_id}")

asyncio.run(main())
```

### File Sharing

```python
async with EntangleMatrixClient("http://localhost:8000") as client:
    # Send an image with caption
    upload = await client.send_image(
        room_id="!roomid:example.com",
        image_path="/path/to/image.png",
        caption="Check out this image! 📸"
    )

    # Send an audio file
    await client.send_audio(
        room_id="!roomid:example.com",
        audio_path="/path/to/audio.mp3",
        caption="🎵 Here's an audio message"
    )
```

### Room Management

```python
async with EntangleMatrixClient("http://localhost:8000") as client:
    # Create a new room
    room = await client.create_room(
        name="My SDK Room",
        topic="Created with Entangle SDK",
        is_public=False
    )

    # List all rooms
    rooms = await client.list_rooms()
    for room in rooms:
        print(f"Room: {room.name} ({room.member_count} members)")

    # Join a room
    joined_room = await client.join_room("#example:matrix.org")
```

## 📖 API Reference

### EntangleMatrixClient

The main client class for interacting with the Entangle Matrix API.

#### Constructor

```python
EntangleMatrixClient(
    base_url: str,
    api_key: Optional[str] = None,
    timeout: int = 30,
    max_file_size_mb: int = 10
)
```

- `base_url`: Base URL of your Entangle API server
- `api_key`: Optional API key for authentication
- `timeout`: Request timeout in seconds (default: 30)
- `max_file_size_mb`: Maximum file size for uploads in MB (default: 10)

#### Methods

##### Messaging

- **`send_message(room_id, message, formatted_body=None, format_type=None)`**
  - Send a text message to a Matrix room
  - Returns: `MatrixMessage`

- **`send_image(room_id, image_path, caption=None)`**
  - Send an image file to a Matrix room
  - Returns: `MatrixUpload`

- **`send_audio(room_id, audio_path, caption=None)`**
  - Send an audio file to a Matrix room
  - Returns: `MatrixUpload`

- **`send_file(room_id, file_path, caption=None)`**
  - Send a generic file to a Matrix room
  - Returns: `MatrixUpload`

##### Room Management

- **`create_room(name, topic=None, is_public=False, is_direct=False, invite_users=None)`**
  - Create a new Matrix room
  - Returns: `MatrixRoom`

- **`join_room(room_id_or_alias)`**
  - Join an existing Matrix room
  - Returns: `MatrixRoom`

- **`list_rooms()`**
  - Get list of all joined rooms
  - Returns: `List[MatrixRoom]`

- **`get_room_info(room_id)`**
  - Get detailed information about a room
  - Returns: `MatrixRoom`

##### Utility

- **`health_check()`**
  - Check API server health status
  - Returns: `Dict[str, Any]`

### Data Models

#### MatrixMessage
```python
@dataclass
class MatrixMessage:
    event_id: str
    room_id: str
    timestamp: str
    message: str
    metadata: Optional[Dict[str, Any]] = None
```

#### MatrixUpload
```python
@dataclass
class MatrixUpload:
    event_id: str
    room_id: str
    mxc_uri: str
    file_name: str
    file_size: int
    content_type: str
    metadata: Optional[Dict[str, Any]] = None
```

#### MatrixRoom
```python
@dataclass
class MatrixRoom:
    room_id: str
    name: Optional[str]
    topic: Optional[str]
    avatar_url: Optional[str]
    member_count: int
    is_encrypted: bool
    is_direct: bool
    metadata: Optional[Dict[str, Any]] = None
```

## 🔧 Error Handling

The SDK provides a comprehensive exception hierarchy:

```python
from entangle_matrix import (
    EntangleMatrixError,      # Base exception
    AuthenticationError,      # HTTP 401
    ValidationError,          # HTTP 400
    NotFoundError,           # HTTP 404
    RateLimitError,          # HTTP 429
    ServerError,             # HTTP 500+
    NetworkError             # Network issues
)

try:
    message = await client.send_message(room_id, "Hello!")
except AuthenticationError:
    print("Invalid API key")
except ValidationError as e:
    print(f"Invalid input: {e.message}")
except NetworkError as e:
    print(f"Network problem: {e.message}")
except EntangleMatrixError as e:
    print(f"Matrix API error: {e.message}")
```

## 🧪 Examples

Check out the [examples](./examples/) directory for more detailed usage examples:

- [`basic_usage.py`](./examples/basic_usage.py) - Basic messaging and room listing
- [`file_sharing.py`](./examples/file_sharing.py) - Image, audio, and file uploads
- [`room_management.py`](./examples/room_management.py) - Creating and managing rooms

## 🛠️ Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/qbit-codes/entangle-python-client.git
cd entangle-python-client

# Install in development mode
pip install -e .[dev]
```

### Running Tests

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=entangle_matrix --cov-report=html

# Run type checking
mypy entangle_matrix/

# Format code
black entangle_matrix/
isort entangle_matrix/
```

### Building the Package

```bash
# Build source and wheel distributions
python -m build

# Upload to PyPI (maintainers only)
twine upload dist/*
```

## 📋 Requirements

- Python 3.9+
- aiohttp >= 3.8.0
- aiofiles >= 23.2.1

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [Documentation](https://github.com/qbit-codes/entangle-python-client#readme)
- [PyPI Package](https://pypi.org/project/entangle-matrix/)
- [Issue Tracker](https://github.com/qbit-codes/entangle-python-client/issues)
- [Source Code](https://github.com/qbit-codes/entangle-python-client)

## 🙏 Acknowledgments

Built with ❤️ by [QBit Codes](https://github.com/qbit-codes) for the Entangle Matrix API platform.