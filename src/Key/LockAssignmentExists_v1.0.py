from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class LockAssignmentExistsRequest(CamelCaseModel):
    key_id: str = Field(
        ...,
        title="Key ID",
        description="UID of a key as a hex encoded string without delimiters.",
        examples=["a1b2c3d4e5f6890"],
        min_length=1,
        pattern=r"^[0-9a-f]+$",
    )
    lock_id: str = Field(
        ...,
        title="Lock ID",
        description="Vendor specific ID for a lock.",
        examples=["12345678"],
        min_length=1,
    )
    shared_secret: str = Field(
        ...,
        title="Shared Secret",
        description="Shared secret between the productizer and the system using it.",
    )


class LockAssignmentExistsResponse(CamelCaseModel):
    exists: bool = Field(
        ...,
        title="Exists",
        description="Whether a matching assignment exists or not.",
        examples=[True],
    )


DEFINITION = DataProductDefinition(
    version="1.0.1",
    title="Check if lock assignment exists",
    description="Check if a key has access to a specific lock.",
    tags=["Housing"],
    request=LockAssignmentExistsRequest,
    response=LockAssignmentExistsResponse,
)
