from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.api.dependencies import get_current_user
from app.database.connection import get_db
from app.database.models import Application, ApplicationEvent, User
from app.schemas.application import EventOut
router = APIRouter(prefix="/timeline", tags=["Timeline"])
@router.get("/{application_id}", response_model=list[EventOut])
def timeline(application_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    app = db.scalar(select(Application).where(Application.id == application_id, Application.user_id == user.id))
    if not app: raise HTTPException(status_code=404, detail="Application not found")
    return list(db.scalars(select(ApplicationEvent).where(ApplicationEvent.application_id == application_id).order_by(ApplicationEvent.created_at.asc())).all())
