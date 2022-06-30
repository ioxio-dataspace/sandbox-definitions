from converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class DeleteAssignmentResponse(CamelCaseModel):
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


class DeleteAssignmentRequest(DeleteAssignmentResponse):
    shared_secret: str = Field(
        ...,
        title="Shared Secret",
        description="Shared secret between the productizer and the system using it",
    )


DEFINITION = DataProductDefinition(
    description="Delete key assignment",
    request=DeleteAssignmentRequest,
    response=DeleteAssignmentResponse,
    route_description="Delete assignment",
    summary="Delete key assignment",
)
