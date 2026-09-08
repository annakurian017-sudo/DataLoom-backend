import uuid
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.services import dataset_service as service


from app.schemas import DatasetCreate


def create_dataset(db: Session, dataset: DatasetCreate):
    return service.create_dataset(db, dataset)


def get_datasets(db: Session):
    return service.get_datasets(db)


def get_dataset(db: Session, dataset_id: uuid.UUID):
    dataset = service.get_dataset(db, dataset_id)
    if dataset is None:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return dataset


def update_dataset(db: Session, dataset_id: uuid.UUID, dataset: DatasetCreate):
    updated = service.update_dataset(db, dataset_id, dataset)
    if updated is None:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return updated


def delete_dataset(db: Session, dataset_id: uuid.UUID):
    dataset = service.delete_dataset(db, dataset_id)
    if dataset is None:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return {"message": "Dataset deleted successfully"}