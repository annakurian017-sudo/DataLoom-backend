from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session  

from app.schemas import ProcessCreate, ProcessResponse
from app.database import get_db
from app.services import process_service as service
import uuid

router = APIRouter(
    tags=["Process"],
    prefix="/process"
)

# CREATE
@router.post("", response_model=ProcessResponse)
def create_process(
    process: ProcessCreate,
    db: Session = Depends(get_db)
):
    print("Creating process:", process)
    return service.create_process(db, process)


# READ ALL
@router.get("", response_model=list[ProcessResponse])
def get_processes(
    db: Session = Depends(get_db)
):
    return service.get_processes(db)

# READ ONE
@router.get("/{process_id}", response_model=ProcessResponse)
def get_process(
    process_id: str,
    db: Session = Depends(get_db)
):
    process = service.get_process(db, process_id)

    if process is None:
        raise HTTPException(
            status_code=404,
            detail="Process not found"
        )

    return process

# UPDATE
@router.put(
    "/process/{process_id}",
    response_model=ProcessResponse
)
def update_process(
    process_id: uuid.UUID,
    process: ProcessCreate,
    db: Session = Depends(get_db)
):
    updated_process = service.update_process(
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

# DELETE
@router.delete("/{process_id}")
def delete_process(
    process_id: uuid.UUID,
    db: Session = Depends(get_db)
):
    process = service.delete_process(
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