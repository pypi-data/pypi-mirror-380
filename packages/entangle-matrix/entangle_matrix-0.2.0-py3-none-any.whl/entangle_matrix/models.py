"""
Data models for the Entangle Matrix SDK.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional, List, Dict, Any
from datetime import datetime


class CallSampleType(Enum):
    HUMAN = "human"
    FIRE = "fire"


@dataclass
class MatrixMessage:
    """Represents a Matrix message response."""

    event_id: str
    room_id: str
    timestamp: str
    message: str
    metadata: Optional[Dict[str, Any]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MatrixMessage":
        """Create MatrixMessage from API response data."""
        return cls(
            event_id=data["event_id"],
            room_id=data["room_id"],
            timestamp=data["timestamp"],
            message=data["message"],
            metadata=data.get("metadata", {}),
        )


@dataclass
class MatrixVoiceCall:
    """Represents a Matrix voice call response."""

    call_id: str
    room_id: str
    target_user: str
    state: str
    audio_source: str
    initiated_at: datetime

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MatrixVoiceCall":
        """Create MatrixVoiceCall from API response data."""
        return cls(
            call_id=data["call_id"],
            room_id=data["room_id"],
            target_user=data["target_user"],
            state=data["state"],
            audio_source=data["audio_source"],
            initiated_at=data["initiated_at"],
        )


@dataclass
class MatrixUpload:
    """Represents a Matrix media upload response."""

    event_id: str
    room_id: str
    mxc_uri: str
    file_name: str
    file_size: int
    content_type: str
    metadata: Optional[Dict[str, Any]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MatrixUpload":
        """Create MatrixUpload from API response data."""
        return cls(
            event_id=data["event_id"],
            room_id=data["room_id"],
            mxc_uri=data["mxc_uri"],
            file_name=data["file_name"],
            file_size=data["file_size"],
            content_type=data["content_type"],
            metadata=data.get("metadata", {}),
        )


@dataclass
class MatrixRoom:
    """Represents a Matrix room."""

    room_id: str
    name: Optional[str]
    topic: Optional[str]
    avatar_url: Optional[str]
    member_count: int
    is_encrypted: bool
    is_direct: bool
    metadata: Optional[Dict[str, Any]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MatrixRoom":
        """Create MatrixRoom from API response data."""
        return cls(
            room_id=data["room_id"],
            name=data.get("name"),
            topic=data.get("topic"),
            avatar_url=data.get("avatar_url"),
            member_count=data["member_count"],
            is_encrypted=data["is_encrypted"],
            is_direct=data["is_direct"],
            metadata=data.get("metadata", {}),
        )


@dataclass
class MessageRequest:
    """Request data for sending a message."""

    room_id: str
    message: str
    formatted_body: Optional[str] = None
    format_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API request."""
        data = {
            "room_id": self.room_id,
            "message": self.message,
        }
        if self.formatted_body:
            data["formatted_body"] = self.formatted_body
        if self.format_type:
            data["format_type"] = self.format_type
        return data


@dataclass
class InitiateCallRequest:
    """Request data for initiating call."""

    room_id: str
    target_user: str
    sample_type: Optional[CallSampleType] = None
    call_timeout: Optional[int] = 120000
    auto_hangup_after: Optional[int] = 60

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API request."""
        data: Dict[str, Any] = {
            "room_id": self.room_id,
            "target_user": self.target_user,
        }
        if self.call_timeout:
            data["call_timeout"] = str(self.call_timeout)
        if self.auto_hangup_after:
            data["auto_hangup_after"] = str(self.auto_hangup_after)
        if self.sample_type and isinstance(self.sample_type, Enum):
            data["sample_type"] = self.sample_type.value
        return data


@dataclass
class CreateRoomRequest:
    """Request data for creating a room."""

    name: str
    topic: Optional[str] = None
    is_public: bool = False
    is_direct: bool = False
    invite_users: Optional[List[str]] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API request."""
        data = {
            "name": self.name,
            "is_public": self.is_public,
            "is_direct": self.is_direct,
        }
        if self.topic:
            data["topic"] = self.topic
        if self.invite_users:
            data["invite_users"] = self.invite_users
        return data


@dataclass
class JoinRoomRequest:
    """Request data for joining a room."""

    room_id_or_alias: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API request."""
        return {"room_id_or_alias": self.room_id_or_alias}


@dataclass
class APIResponse:
    """Standard API response wrapper."""

    success: bool
    message: str
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "APIResponse":
        """Create APIResponse from response data."""
        return cls(
            success=data.get("success", False),
            message=data.get("message", ""),
            data=data.get("data"),
            error=data.get("error"),
        )
