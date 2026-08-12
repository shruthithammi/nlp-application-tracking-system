from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from app.api.dependencies import get_current_user
from app.database.connection import get_db
from app.database.models import Application, User
from app.schemas.application import ApplicationCreate, ApplicationUpdate, ApplicationOut
from app.services.application_service import create_application, update_status

router = APIRouter(prefix="/applications", tags=["Applications"])

@router.post("", response_model=ApplicationOut, status_code=201)
def create(payload: ApplicationCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return create_application(db, user.id, payload.company, payload.role, payload.applied_date or datetime.now(timezone.utc))

@router.get("", response_model=list[ApplicationOut])
def list_all(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    stmt = select(Application).where(Application.user_id == user.id).options(selectinload(Application.events)).order_by(Application.applied_date.desc())
    return list(db.scalars(stmt).unique().all())

@router.get("/{application_id}", response_model=ApplicationOut)
def get_one(application_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    stmt = select(Application).where(Application.id == application_id, Application.user_id == user.id).options(selectinload(Application.events))
    app = db.scalar(stmt)
    if not app: raise HTTPException(status_code=404, detail="Application not found")
    return app

@router.patch("/{application_id}", response_model=ApplicationOut)
def update(application_id: int, payload: ApplicationUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    app = db.scalar(select(Application).where(Application.id == application_id, Application.user_id == user.id))
    if not app: raise HTTPException(status_code=404, detail="Application not found")
    if payload.status:
        return update_status(db, app, payload.status, payload.latest_explanation or f"Status changed to {payload.status}.")
    if payload.latest_explanation is not None: app.latest_explanation = payload.latest_explanation
    db.commit(); db.refresh(app); return app
