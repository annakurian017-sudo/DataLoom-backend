from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from app.database import get_db
from app.models import Process, Dataset

router = APIRouter(tags=["Health"], prefix="/health_check")

@router.get("")
def health_check():
    return {"status": "healthy"}


@router.get("/db_health")
def db_health(
    db: Session = Depends(get_db)
):
    try:
        # Check all tables using ORM queries
        db.query(Process).first()
        db.query(Dataset).first()

        return {
            "status": "healthy",
            "database": "connected",
            "tables": {
                "process": "healthy",
                "dataset": "healthy"
            }
        }

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "unhealthy",
                "database": "disconnected",
                "error": str(e)
            }
        )