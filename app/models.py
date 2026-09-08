import uuid

from sqlalchemy import Column, String, JSON
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class Process(Base):
    __tablename__ = "process"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False
    )

    name = Column(
        String,
        nullable=False
    )


class Dataset(Base):
    __tablename__ = "dataset"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False
    )

    name = Column(
        String,
        nullable=False
    )

    uploaded_xl = Column(
        String,
        nullable=True
    )

    dataset_config = Column(
        JSON,
        nullable=True
    )
    