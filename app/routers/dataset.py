from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session  

from app.schemas import DatasetCreate, DatasetResponse
from app.database import get_db
from app.services import dataset_service as service
import uuid

router = APIRouter(
    tags=["Dataset"],
    prefix="/dataset"
)


# CREATE
@router.post("", response_model=DatasetResponse)
def create_dataset(
    dataset: DatasetCreate,
    db: Session = Depends(get_db)
):
    return service.create_dataset(db, dataset)


# READ ALL
@router.get("", response_model=list[DatasetResponse])
def get_datasets(
    db: Session = Depends(get_db)
):
    return service.get_datasets(db)

# READ ONE
@router.get("/{dataset_id}", response_model=DatasetResponse)
def get_dataset(
    dataset_id: uuid.UUID,
    db: Session = Depends(get_db)
):
    dataset = service.get_dataset(db, dataset_id)

    if dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found"
        )

    return dataset

# UPDATE
@router.put("/{dataset_id}", response_model=DatasetResponse)
def update_dataset(
    dataset_id: uuid.UUID,
    dataset: DatasetCreate,
    db: Session = Depends(get_db)
):
    updated_dataset = service.update_dataset(
        db,
        dataset_id,
        dataset
    )

    if updated_dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found"
        )

    return updated_dataset

# DELETE
@router.delete("/{dataset_id}")
def delete_dataset(
    dataset_id: uuid.UUID,
    db: Session = Depends(get_db)
):
    dataset = service.delete_dataset(
        db,
        dataset_id
    )

    if dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found"
        )

    return {
        "message": "Dataset deleted successfully"
    }