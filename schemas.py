import uuid
from typing import Any

from pydantic import BaseModel, ConfigDict


# -------------------------
# Process
# -------------------------

class ProcessCreate(BaseModel):
    name: str


class ProcessResponse(BaseModel):
    id: uuid.UUID
    name: str

    model_config = ConfigDict(from_attributes=True)


# -------------------------
# Dataset
# -------------------------

class DatasetCreate(BaseModel):
    name: str
    uploaded_xl: str | None = None
    dataset_config: dict[str, Any] | None = None


class DatasetResponse(BaseModel):
    id: uuid.UUID
    name: str
    uploaded_xl: str | None = None
    dataset_config: dict[str, Any] | None = None

    model_config = ConfigDict(from_attributes=True)