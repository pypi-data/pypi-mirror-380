# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerificationCheckResponse", "Metadata"]


class Metadata(BaseModel):
    correlation_id: Optional[str] = None
    """A user-defined identifier to correlate this verification with.

    It is returned in the response and any webhook events that refer to this
    verification.
    """


class VerificationCheckResponse(BaseModel):
    status: Literal["success", "failure", "expired_or_not_found"]
    """The status of the check."""

    id: Optional[str] = None
    """The verification identifier."""

    metadata: Optional[Metadata] = None
    """The metadata for this verification."""

    request_id: Optional[str] = None
