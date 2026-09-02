from sqlalchemy.orm import Session

from models import Process, Dataset
from schemas import ProcessCreate, DatasetCreate


# =========================
# PROCESS CRUD
# =========================

def create_process(db: Session, process: ProcessCreate):
    db_process = Process(
        name=process.name
    )

    db.add(db_process)
    db.commit()
    db.refresh(db_process)

    return db_process


def get_processes(db: Session):
    return db.query(Process).all()


def get_process(db: Session, process_id):
    return db.query(Process).filter(
        Process.id == process_id
    ).first()


def update_process(db: Session, process_id, process: ProcessCreate):
    db_process = get_process(db, process_id)

    if db_process is None:
        return None

    db_process.name = process.name

    db.commit()
    db.refresh(db_process)

    return db_process


def delete_process(db: Session, process_id):
    db_process = get_process(db, process_id)

    if db_process is None:
        return None

    db.delete(db_process)
    db.commit()

    return db_process


# =========================
# DATASET CRUD
# =========================

def create_dataset(db: Session, dataset: DatasetCreate):
    db_dataset = Dataset(
        name=dataset.name,
        uploaded_xl=dataset.uploaded_xl,
        dataset_config=dataset.dataset_config
    )

    db.add(db_dataset)
    db.commit()
    db.refresh(db_dataset)

    return db_dataset


def get_datasets(db: Session):
    return db.query(Dataset).all()


def get_dataset(db: Session, dataset_id):
    return db.query(Dataset).filter(
        Dataset.id == dataset_id
    ).first()


def update_dataset(db: Session, dataset_id, dataset: DatasetCreate):
    db_dataset = get_dataset(db, dataset_id)

    if db_dataset is None:
        return None

    db_dataset.name = dataset.name
    db_dataset.uploaded_xl = dataset.uploaded_xl
    db_dataset.dataset_config = dataset.dataset_config

    db.commit()
    db.refresh(db_dataset)

    return db_dataset


def delete_dataset(db: Session, dataset_id):
    db_dataset = get_dataset(db, dataset_id)

    if db_dataset is None:
        return None

    db.delete(db_dataset)
    db.commit()

    return db_dataset