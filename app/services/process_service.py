import uuid
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models import Process
from app.schemas import ProcessCreate


def create_process(db: Session, process: ProcessCreate):
    db_process = Process(**process.dict())
    db.add(db_process)
    db.commit()
    db.refresh(db_process)
    return db_process


def get_processes(db: Session):
    return db.query(Process).all()


def get_process(db: Session, process_id: uuid.UUID):
    process = db.query(Process).filter(Process.id == process_id).first()
    if process is None:
        raise HTTPException(status_code=404, detail="Process not found")
    return process


def update_process(db: Session, process_id: uuid.UUID, process: ProcessCreate):
    db_process = db.query(Process).filter(Process.id == process_id).first()
    if db_process is None:
        raise HTTPException(status_code=404, detail="Process not found")
    for key, value in process.dict().items():
        setattr(db_process, key, value)
    db.commit()
    db.refresh(db_process)
    return db_process


def delete_process(db: Session, process_id: uuid.UUID):
    db_process = db.query(Process).filter(Process.id == process_id).first()
    if db_process is None:
        raise HTTPException(status_code=404, detail="Process not found")
    db.delete(db_process)
    db.commit()
    return {"message": "Process deleted successfully"}