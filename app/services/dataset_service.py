import uuid
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models import Dataset
from app.schemas import DatasetCreate


def create_dataset(db: Session, dataset: DatasetCreate):
    db_dataset = Dataset(**dataset.dict())
    db.add(db_dataset)
    db.commit()
    db.refresh(db_dataset)
    return db_dataset


def get_datasets(db: Session):
    return db.query(Dataset).all()


def get_dataset(db: Session, dataset_id: uuid.UUID):
    dataset = db.query(Dataset).filter(Dataset.id == dataset_id).first()
    if dataset is None:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return dataset


def update_dataset(db: Session, dataset_id: uuid.UUID, dataset: DatasetCreate):
    db_dataset = db.query(Dataset).filter(Dataset.id == dataset_id).first()
    if db_dataset is None:
        raise HTTPException(status_code=404, detail="Dataset not found")
    for key, value in dataset.dict().items():
        setattr(db_dataset, key, value)
    db.commit()
    db.refresh(db_dataset)
    return db_dataset


def delete_dataset(db: Session, dataset_id: uuid.UUID):
    db_dataset = db.query(Dataset).filter(Dataset.id == dataset_id).first()
    if db_dataset is None:
        raise HTTPException(status_code=404, detail="Dataset not found")
    db.delete(db_dataset)
    db.commit()
    return {"message": "Dataset deleted successfully"}