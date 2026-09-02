import uuid
import models
import crud

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine,Base, get_db
from schemas import (ProcessCreate,ProcessResponse, DatasetCreate, DatasetResponse)

app = FastAPI(
    title="DataLoom API",
    version="1.0.0"
)

@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check():
    return {"status": "ok"}


# =====================================================
# PROCESS
# =====================================================

@app.post(
    "/process",
    response_model=ProcessResponse
)
def create_process(
    process: ProcessCreate,
    db: Session = Depends(get_db)
):
    return crud.create_process(db, process)


@app.get(
    "/process",
    response_model=list[ProcessResponse]
)
def get_processes(
    db: Session = Depends(get_db)
):
    return crud.get_processes(db)


@app.get(
    "/process/{process_id}",
    response_model=ProcessResponse
)
def get_process(
    process_id: uuid.UUID,
    db: Session = Depends(get_db)
):
    process = crud.get_process(db, process_id)

    if process is None:
        raise HTTPException(
            status_code=404,
            detail="Process not found"
        )

    return process


@app.put(
    "/process/{process_id}",
    response_model=ProcessResponse
)
def update_process(
    process_id: uuid.UUID,
    process: ProcessCreate,
    db: Session = Depends(get_db)
):
    updated_process = crud.update_process(
        db,
        process_id,
        process
    )

    if updated_process is None:
        raise HTTPException(
            status_code=404,
            detail="Process not found"
        )

    return updated_process


@app.delete(
    "/process/{process_id}"
)
def delete_process(
    process_id: uuid.UUID,
    db: Session = Depends(get_db)
):
    process = crud.delete_process(
        db,
        process_id
    )

    if process is None:
        raise HTTPException(
            status_code=404,
            detail="Process not found"
        )

    return {
        "message": "Process deleted successfully"
    }


# =====================================================
# DATASET
# =====================================================

@app.post(
    "/dataset",
    response_model=DatasetResponse
)
def create_dataset(
    dataset: DatasetCreate,
    db: Session = Depends(get_db)
):
    return crud.create_dataset(db, dataset)


@app.get(
    "/dataset",
    response_model=list[DatasetResponse]
)
def get_datasets(
    db: Session = Depends(get_db)
):
    return crud.get_datasets(db)


@app.get(
    "/dataset/{dataset_id}",
    response_model=DatasetResponse
)
def get_dataset(
    dataset_id: uuid.UUID,
    db: Session = Depends(get_db)
):
    dataset = crud.get_dataset(db, dataset_id)

    if dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found"
        )

    return dataset


@app.put(
    "/dataset/{dataset_id}",
    response_model=DatasetResponse
)
def update_dataset(
    dataset_id: uuid.UUID,
    dataset: DatasetCreate,
    db: Session = Depends(get_db)
):
    updated_dataset = crud.update_dataset(
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


@app.delete(
    "/dataset/{dataset_id}"
)
def delete_dataset(
    dataset_id: uuid.UUID,
    db: Session = Depends(get_db)
):
    dataset = crud.delete_dataset(
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