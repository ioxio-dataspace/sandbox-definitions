from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class LockAssignmentExistsRequest(CamelCaseModel):
    key_id: str = Field(
        ...,
        title="Key ID",
        description="UID of a key as a hex encoded string without delimiters",
        example="a1b2c3d4e5f6890",
        min_length=1,
        regex=r"^[0-9a-f]+$",
    )
    lock_id: str = Field(
        ...,
        title="Lock ID",
        description="Vendor specific ID for a lock",
        example="12345678",
        min_length=1,
    )
    shared_secret: str = Field(
        ...,
        title="Shared Secret",
        description="Shared secret between the productizer and the system using it",
    )


class LockAssignmentExistsResponse(CamelCaseModel):
    exists: bool = Field(
        ...,
        title="Exists",
        description="Whether a matching assignment exists or not",
        example=True,
    )


DEFINITION = DataProductDefinition(
    title="Check if lock assignment exists",
    description="Check if lock assignment exists",
    request=LockAssignmentExistsRequest,
    response=LockAssignmentExistsResponse,
)
