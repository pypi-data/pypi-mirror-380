"""
Tests for the Entangle Matrix client.
"""

import asyncio
import pytest
from unittest.mock import AsyncMock, patch
from pathlib import Path

from entangle_matrix import EntangleMatrixClient
from entangle_matrix.exceptions import ValidationError, EntangleMatrixError


class TestEntangleMatrixClient:
    """Test cases for EntangleMatrixClient."""

    def test_client_init(self):
        """Test client initialization."""
        client = EntangleMatrixClient(
            base_url="http://localhost:8000",
            api_key="test-key",
            timeout=60,
            max_file_size_mb=20
        )

        assert client.base_url == "http://localhost:8000"
        assert client.api_key == "test-key"
        assert client.max_file_size_mb == 20
        assert client.session is None

    def test_base_url_trailing_slash_removal(self):
        """Test that trailing slashes are removed from base_url."""
        client = EntangleMatrixClient("http://localhost:8000/")
        assert client.base_url == "http://localhost:8000"

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test async context manager usage."""
        with patch('aiohttp.ClientSession') as mock_session:
            mock_session.return_value.closed = False
            mock_session.return_value.close = AsyncMock()

            async with EntangleMatrixClient("http://localhost:8000") as client:
                assert client is not None

            mock_session.return_value.close.assert_called_once()

    def test_validate_room_id(self):
        """Test room ID validation."""
        client = EntangleMatrixClient("http://localhost:8000")

        # Valid room IDs should not raise
        valid_room_ids = [
            "!roomid:example.com",
            "!abc123:matrix.org",
            "!test_room:localhost"
        ]

        # Invalid room IDs should raise ValidationError
        invalid_room_ids = [
            "roomid:example.com",  # Missing !
            "!roomid",             # Missing domain
            "@user:example.com",   # Wrong prefix
            "",                    # Empty
            "invalid"              # No format
        ]

        # Test by trying to send a message (which validates room ID)
        for room_id in invalid_room_ids:
            with pytest.raises(ValidationError):
                # This should raise before making any HTTP request
                asyncio.run(client.send_message(room_id, "test"))

    @pytest.mark.asyncio
    async def test_send_message_validation(self):
        """Test message sending input validation."""
        client = EntangleMatrixClient("http://localhost:8000")

        # Empty message should raise ValidationError
        with pytest.raises(ValidationError, match="Message cannot be empty"):
            await client.send_message("!room:example.com", "")

        # Whitespace-only message should raise ValidationError
        with pytest.raises(ValidationError, match="Message cannot be empty"):
            await client.send_message("!room:example.com", "   ")

        # Invalid room ID should raise ValidationError
        with pytest.raises(ValidationError, match="Invalid room ID format"):
            await client.send_message("invalid-room", "test message")

    @pytest.mark.asyncio
    async def test_file_validation(self):
        """Test file validation for uploads."""
        client = EntangleMatrixClient("http://localhost:8000")

        # Non-existent file should raise ValidationError
        with pytest.raises(ValidationError, match="file not found"):
            await client.send_image("!room:example.com", "/non/existent/file.png")

        # Invalid room ID should raise ValidationError
        with pytest.raises(ValidationError, match="Invalid room ID format"):
            await client.send_image("invalid-room", "test.png")

    @pytest.mark.asyncio
    @patch('entangle_matrix.client.Path.exists', return_value=True)
    @patch('entangle_matrix.utils.is_image_file', return_value=False)
    async def test_non_image_file_validation(self, mock_is_image, mock_exists):
        """Test validation when file is not an image."""
        client = EntangleMatrixClient("http://localhost:8000")

        with pytest.raises(ValidationError, match="File is not an image"):
            await client.send_image("!room:example.com", "not-an-image.txt")

    def test_room_creation_validation(self):
        """Test room creation input validation."""
        client = EntangleMatrixClient("http://localhost:8000")

        # Empty name should raise ValidationError
        with pytest.raises(ValidationError, match="Room name cannot be empty"):
            asyncio.run(client.create_room(""))

        # Whitespace-only name should raise ValidationError
        with pytest.raises(ValidationError, match="Room name cannot be empty"):
            asyncio.run(client.create_room("   "))

    def test_join_room_validation(self):
        """Test room joining input validation."""
        client = EntangleMatrixClient("http://localhost:8000")

        # Empty room ID should raise ValidationError
        with pytest.raises(ValidationError, match="Room ID or alias cannot be empty"):
            asyncio.run(client.join_room(""))

        # Whitespace-only room ID should raise ValidationError
        with pytest.raises(ValidationError, match="Room ID or alias cannot be empty"):
            asyncio.run(client.join_room("   "))

    @pytest.mark.asyncio
    async def test_error_handling(self):
        """Test error handling for different HTTP status codes."""
        with patch('aiohttp.ClientSession') as mock_session:
            # Mock response for 401 error
            mock_response = AsyncMock()
            mock_response.status = 401
            mock_response.content_type = "application/json"
            mock_response.json = AsyncMock(return_value={"detail": "Unauthorized"})

            mock_session.return_value.request.return_value.__aenter__.return_value = mock_response
            mock_session.return_value.closed = False

            client = EntangleMatrixClient("http://localhost:8000")

            with pytest.raises(EntangleMatrixError):
                await client.health_check()

    @pytest.mark.asyncio
    async def test_successful_health_check(self):
        """Test successful health check."""
        expected_response = {"status": "healthy", "version": "1.0.0"}

        with patch('aiohttp.ClientSession') as mock_session:
            mock_response = AsyncMock()
            mock_response.status = 200
            mock_response.content_type = "application/json"
            mock_response.json = AsyncMock(return_value=expected_response)

            mock_session.return_value.request.return_value.__aenter__.return_value = mock_response
            mock_session.return_value.closed = False

            client = EntangleMatrixClient("http://localhost:8000")
            result = await client.health_check()

            assert result == expected_response


if __name__ == "__main__":
    pytest.main([__file__])