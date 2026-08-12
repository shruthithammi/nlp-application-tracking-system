from sqlalchemy.orm import Session
from app.database.models import Notification

def create_notification(db: Session, user_id: int, message: str):
    item = Notification(user_id=user_id, message=message)
    db.add(item); db.commit(); db.refresh(item); return item
