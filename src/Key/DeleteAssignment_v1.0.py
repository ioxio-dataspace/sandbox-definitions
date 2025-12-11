from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import ConfigDict, Field


class DeleteAssignmentResponse(CamelCaseModel):
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

    model_config: ConfigDict = ConfigDict(title="Delete assignment response")


class DeleteAssignmentRequest(DeleteAssignmentResponse):
    shared_secret: str = Field(
        ...,
        title="Shared Secret",
        description="Shared secret between the data source and the system using it.",
    )

    model_config: ConfigDict = ConfigDict(title="Delete assignment request")


DEFINITION = DataProductDefinition(
    version="1.0.4",
    strict_validation=False,
    title="Delete key assignment",
    description="Remove a key from having access to a specific lock.",
    tags=["Housing"],
    request=DeleteAssignmentRequest,
    response=DeleteAssignmentResponse,
)
