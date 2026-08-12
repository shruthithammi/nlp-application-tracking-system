from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.api.dependencies import get_current_user
from app.database.connection import get_db
from app.database.models import Notification, User
from app.schemas.notification import NotificationOut
router = APIRouter(prefix="/notifications", tags=["Notifications"])
@router.get("", response_model=list[NotificationOut])
def notifications(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return list(db.scalars(select(Notification).where(Notification.user_id == user.id).order_by(Notification.created_at.desc())).all())
