"""
Main client for the Entangle Matrix SDK.
"""

import asyncio
from dataclasses import dataclass
import aiohttp
import aiofiles
from pathlib import Path
from typing import Optional, List, Dict, Any

from .models import (
    CallSampleType,
    InitiateCallRequest,
    MatrixMessage,
    MatrixUpload,
    MatrixRoom,
    MatrixVoiceCall,
    MessageRequest,
    CreateRoomRequest,
    JoinRoomRequest,
    APIResponse,
)
from .exceptions import (
    EntangleMatrixError,
    AuthenticationError,
    NetworkError,
    ValidationError,
    NotFoundError,
    RateLimitError,
    ServerError,
)
from .utils import (
    get_content_type,
    validate_room_id,
    validate_file_size,
    is_image_file,
    is_audio_file,
    validate_user_id,
)


class EntangleMatrixClient:
    """
    Async client for Entangle Matrix API.

    This client provides methods to interact with the Entangle Matrix API
    for sending messages, uploading media, and managing rooms.

    Example:
        ```python
        async with EntangleMatrixClient(
            base_url="http://localhost:8000",
            api_key="your-api-key"
        ) as client:
            # Send a message
            message = await client.send_message("!room:example.com", "Hello!")

            # Send an image
            upload = await client.send_image("!room:example.com", "/path/to/image.png")

            # Initiate a voice call
            call = await client.initiate_call(
                "!room:example.com",
                "@user:example.com",
                CallSampleType.HUMAN
            )

            # List rooms
            rooms = await client.list_rooms()
        ```
    """

    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        timeout: int = 30,
        max_file_size_mb: int = 10,
    ) -> None:
        """
        Initialize the client.

        Args:
            base_url: Base URL of the Entangle API (e.g., "http://localhost:8000")
            api_key: API key for authentication (if required)
            timeout: Request timeout in seconds
            max_file_size_mb: Maximum file size for uploads in MB
        """
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.max_file_size_mb = max_file_size_mb
        self.session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self) -> "EntangleMatrixClient":
        """Async context manager entry."""
        await self._ensure_session()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit."""
        await self.close()

    async def _ensure_session(self) -> None:
        """Ensure aiohttp session is created."""
        if self.session is None or self.session.closed:
            headers = {}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"

            self.session = aiohttp.ClientSession(
                headers=headers,
                timeout=self.timeout,
                connector=aiohttp.TCPConnector(limit=10),
            )

    async def close(self) -> None:
        """Close the HTTP session."""
        if self.session and not self.session.closed:
            await self.session.close()

    async def _request(
        self, method: str, endpoint: str, **kwargs
    ) -> Dict[str, Any]:
        """
        Make an HTTP request to the API.

        Args:
            method: HTTP method
            endpoint: API endpoint
            **kwargs: Additional arguments for aiohttp

        Returns:
            Response data dictionary

        Raises:
            EntangleMatrixError: For API or network errors
        """
        await self._ensure_session()
        url = f"{self.base_url}{endpoint}"

        try:
            async with self.session.request(method, url, **kwargs) as response:
                # Parse response
                if response.content_type == "application/json":
                    data = await response.json()
                else:
                    text = await response.text()
                    data = {"message": text}

                # Handle HTTP errors
                if response.status >= 400:
                    error_msg = data.get(
                        "detail", data.get("message", f"HTTP {response.status}")
                    )

                    if response.status == 401:
                        raise AuthenticationError(error_msg)
                    elif response.status == 404:
                        raise NotFoundError(error_msg)
                    elif response.status == 400:
                        raise ValidationError(error_msg)
                    elif response.status == 429:
                        raise RateLimitError(error_msg)
                    elif response.status >= 500:
                        raise ServerError(error_msg)
                    else:
                        raise EntangleMatrixError(error_msg, response.status)

                return data

        except aiohttp.ClientError as e:
            raise NetworkError(f"Network error: {str(e)}")

    async def health_check(self) -> Dict[str, Any]:
        """
        Check API health status.

        Returns:
            Health status data

        Raises:
            EntangleMatrixError: If health check fails
        """
        return await self._request("GET", "/api/health")

    async def send_message(
        self,
        room_id: str,
        message: str,
        formatted_body: Optional[str] = None,
        format_type: Optional[str] = None,
    ) -> MatrixMessage:
        """
        Send a text message to a Matrix room.

        Args:
            room_id: Matrix room ID (e.g., !roomid:example.com)
            message: Plain text message
            formatted_body: Optional HTML formatted message
            format_type: Optional format type (e.g., "org.matrix.custom.html")

        Returns:
            MatrixMessage object with event details

        Raises:
            ValidationError: If room_id format is invalid
            EntangleMatrixError: If message sending fails
        """
        if not validate_room_id(room_id):
            raise ValidationError(f"Invalid room ID format: {room_id}")

        if not message.strip():
            raise ValidationError("Message cannot be empty")

        request_data = MessageRequest(
            room_id=room_id,
            message=message,
            formatted_body=formatted_body,
            format_type=format_type,
        )

        response = await self._request(
            "POST", "/api/v1/matrix/send-message", json=request_data.to_dict()
        )

        api_response = APIResponse.from_dict(response)
        if not api_response.success:
            raise EntangleMatrixError(f"Message send failed: {api_response.message}")

        return MatrixMessage.from_dict(api_response.data)

    async def send_image(
        self, room_id: str, image_path: str, caption: Optional[str] = None
    ) -> MatrixUpload:
        """
        Send an image to a Matrix room.

        Args:
            room_id: Matrix room ID
            image_path: Path to the image file
            caption: Optional image caption

        Returns:
            MatrixUpload object with upload details

        Raises:
            ValidationError: If room_id format or file is invalid
            EntangleMatrixError: If image sending fails
        """
        if not validate_room_id(room_id):
            raise ValidationError(f"Invalid room ID format: {room_id}")

        image_path = Path(image_path)
        if not image_path.exists():
            raise ValidationError(f"Image file not found: {image_path}")

        if not is_image_file(image_path):
            raise ValidationError(f"File is not an image: {image_path}")

        if not validate_file_size(image_path, self.max_file_size_mb):
            raise ValidationError(
                f"File size exceeds {self.max_file_size_mb}MB limit: {image_path}"
            )

        # Create form data
        data = aiohttp.FormData()
        data.add_field("room_id", room_id)

        if caption:
            data.add_field("caption", caption)

        # Add file
        async with aiofiles.open(image_path, "rb") as f:
            file_content = await f.read()
            data.add_field(
                "image_file",
                file_content,
                filename=image_path.name,
                content_type=get_content_type(image_path),
            )

        response = await self._request("POST", "/api/v1/matrix/send-image", data=data)

        api_response = APIResponse.from_dict(response)
        if not api_response.success:
            raise EntangleMatrixError(f"Image send failed: {api_response.message}")

        return MatrixUpload.from_dict(api_response.data)

    async def send_audio(
        self, room_id: str, audio_path: str, caption: Optional[str] = None
    ) -> MatrixUpload:
        """
        Send an audio file to a Matrix room.

        Args:
            room_id: Matrix room ID
            audio_path: Path to the audio file
            caption: Optional audio caption

        Returns:
            MatrixUpload object with upload details

        Raises:
            ValidationError: If room_id format or file is invalid
            EntangleMatrixError: If audio sending fails
        """
        if not validate_room_id(room_id):
            raise ValidationError(f"Invalid room ID format: {room_id}")

        audio_path = Path(audio_path)
        if not audio_path.exists():
            raise ValidationError(f"Audio file not found: {audio_path}")

        if not is_audio_file(audio_path):
            raise ValidationError(f"File is not an audio file: {audio_path}")

        if not validate_file_size(audio_path, self.max_file_size_mb):
            raise ValidationError(
                f"File size exceeds {self.max_file_size_mb}MB limit: {audio_path}"
            )

        data = aiohttp.FormData()
        data.add_field("room_id", room_id)

        if caption:
            data.add_field("caption", caption)

        async with aiofiles.open(audio_path, "rb") as f:
            file_content = await f.read()
            data.add_field(
                "audio_file",
                file_content,
                filename=audio_path.name,
                content_type=get_content_type(audio_path),
            )

        response = await self._request("POST", "/api/v1/matrix/send-audio", data=data)

        api_response = APIResponse.from_dict(response)
        if not api_response.success:
            raise EntangleMatrixError(f"Audio send failed: {api_response.message}")

        return MatrixUpload.from_dict(api_response.data)

    async def send_file(
        self, room_id: str, file_path: str, caption: Optional[str] = None
    ) -> MatrixUpload:
        """
        Send a file to a Matrix room.

        Args:
            room_id: Matrix room ID
            file_path: Path to the file
            caption: Optional file caption

        Returns:
            MatrixUpload object with upload details

        Raises:
            ValidationError: If room_id format or file is invalid
            EntangleMatrixError: If file sending fails
        """
        if not validate_room_id(room_id):
            raise ValidationError(f"Invalid room ID format: {room_id}")

        file_path = Path(file_path)
        if not file_path.exists():
            raise ValidationError(f"File not found: {file_path}")

        if not validate_file_size(file_path, self.max_file_size_mb):
            raise ValidationError(
                f"File size exceeds {self.max_file_size_mb}MB limit: {file_path}"
            )

        data = aiohttp.FormData()
        data.add_field("room_id", room_id)

        if caption:
            data.add_field("caption", caption)

        async with aiofiles.open(file_path, "rb") as f:
            file_content = await f.read()
            data.add_field(
                "file",
                file_content,
                filename=file_path.name,
                content_type=get_content_type(file_path),
            )

        response = await self._request("POST", "/api/v1/matrix/send-file", data=data)

        api_response = APIResponse.from_dict(response)
        if not api_response.success:
            raise EntangleMatrixError(f"File send failed: {api_response.message}")

        return MatrixUpload.from_dict(api_response.data)

    async def initiate_call(
        self,
        room_id: str,
        target_user: str,
        sample_type: CallSampleType,
        auto_hangup_after: Optional[int] = 60,
        call_timeout: Optional[int] = 120000,
    ) -> MatrixVoiceCall:
        """
        Initiate a voice call to a user in a Matrix room.

        Args:
            room_id: Matrix room ID where the call will be initiated
            target_user: User ID to call
            sample_type: Type of call sample (voice/video)
            auto_hangup_after: Auto hangup timeout in seconds
            call_timeout: Call timeout in milliseconds

        Returns:
            MatrixVoiceCall object with call initiation details

        Raises:
            ValidationError: If room_id or target_user format is invalid
            EntangleMatrixError: If call initiation fails
        """
        if not validate_room_id(room_id):
            raise ValidationError(f"Invalid room ID format: {room_id}")

        if not validate_user_id(target_user):
            raise ValidationError(f"Invalid user ID format: {target_user}")

        request_data = InitiateCallRequest(
            room_id, target_user, sample_type, auto_hangup_after, call_timeout
        ).to_dict()

        data = aiohttp.FormData()
        data.add_field("room_id", request_data.get("room_id"))
        data.add_field("target_user", request_data.get("target_user"))
        data.add_field("sample_type", request_data.get("sample_type", "human"))
        data.add_field("auto_hangup_after", request_data.get("auto_hangup_after", 60))
        data.add_field("call_timeout", request_data.get("call_timeout", 120000))

        response = await self._request(
            "POST", "/api/v1/matrix/voice-call/initiate", data=data
        )

        api_response = APIResponse.from_dict(response)
        if not api_response.success:
            raise EntangleMatrixError(f"Initiate call failed: {api_response.message}")

        if api_response.data is None:
            raise EntangleMatrixError(
                "Initiate call failed for some reason. Data is empty"
            )

        return MatrixVoiceCall.from_dict(api_response.data)

    async def create_room(
        self,
        name: str,
        topic: Optional[str] = None,
        is_public: bool = False,
        is_direct: bool = False,
        invite_users: Optional[List[str]] = None,
    ) -> MatrixRoom:
        """
        Create a new Matrix room.

        Args:
            name: Room name
            topic: Optional room topic
            is_public: Whether room is public
            is_direct: Whether room is direct message
            invite_users: List of user IDs to invite

        Returns:
            MatrixRoom object with room details

        Raises:
            ValidationError: If name is empty or users are invalid
            EntangleMatrixError: If room creation fails
        """
        if not name.strip():
            raise ValidationError("Room name cannot be empty")

        request_data = CreateRoomRequest(
            name=name.strip(),
            topic=topic,
            is_public=is_public,
            is_direct=is_direct,
            invite_users=invite_users,
        )

        response = await self._request(
            "POST", "/api/v1/matrix/create-room", json=request_data.to_dict()
        )

        api_response = APIResponse.from_dict(response)
        if not api_response.success:
            raise EntangleMatrixError(f"Room creation failed: {api_response.message}")

        return MatrixRoom.from_dict(api_response.data)

    async def join_room(self, room_id_or_alias: str) -> MatrixRoom:
        """
        Join a Matrix room.

        Args:
            room_id_or_alias: Room ID or alias to join

        Returns:
            MatrixRoom object with room details

        Raises:
            ValidationError: If room_id_or_alias is empty
            EntangleMatrixError: If room joining fails
        """
        if not room_id_or_alias.strip():
            raise ValidationError("Room ID or alias cannot be empty")

        request_data = JoinRoomRequest(room_id_or_alias=room_id_or_alias.strip())

        response = await self._request(
            "POST", "/api/v1/matrix/join-room", json=request_data.to_dict()
        )

        api_response = APIResponse.from_dict(response)
        if not api_response.success:
            raise EntangleMatrixError(f"Room join failed: {api_response.message}")

        return MatrixRoom.from_dict(api_response.data)

    async def list_rooms(self) -> List[MatrixRoom]:
        """
        Get list of joined Matrix rooms.

        Returns:
            List of MatrixRoom objects

        Raises:
            EntangleMatrixError: If room listing fails
        """
        response = await self._request("GET", "/api/v1/matrix/rooms")

        api_response = APIResponse.from_dict(response)
        if not api_response.success:
            raise EntangleMatrixError(f"Room list failed: {api_response.message}")

        rooms_data = api_response.data["rooms"]
        return [MatrixRoom.from_dict(room) for room in rooms_data]

    async def get_room_info(self, room_id: str) -> MatrixRoom:
        """
        Get information about a specific Matrix room.

        Args:
            room_id: Matrix room ID

        Returns:
            MatrixRoom object with room details

        Raises:
            ValidationError: If room_id format is invalid
            EntangleMatrixError: If room info retrieval fails
        """
        if not validate_room_id(room_id):
            raise ValidationError(f"Invalid room ID format: {room_id}")

        response = await self._request("GET", f"/api/v1/matrix/rooms/{room_id}")

        api_response = APIResponse.from_dict(response)
        if not api_response.success:
            raise EntangleMatrixError(f"Room info failed: {api_response.message}")

        return MatrixRoom.from_dict(api_response.data)
