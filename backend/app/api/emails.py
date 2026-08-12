from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.ai.email_classifier import classifier
from app.ai.status_explainer import explain_status
from app.api.dependencies import get_current_user
from app.database.connection import get_db
from app.database.models import Application, RecruiterEmail, User
from app.schemas.email import EmailAnalyzeRequest, EmailAnalyzeResponse
from app.services.application_service import update_status
from app.services.notification_service import create_notification

router = APIRouter(prefix="/emails", tags=["Recruiter Emails"])
STATUS = {"acknowledgement":"acknowledged", "assessment":"assessment", "interview":"interview", "rejection":"rejected", "offer":"offer"}

@router.post("/analyze", response_model=EmailAnalyzeResponse)
def analyze(payload: EmailAnalyzeRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    app = db.scalar(select(Application).where(Application.id == payload.application_id, Application.user_id == user.id))
    if not app: raise HTTPException(status_code=404, detail="Application not found")
    label, confidence = classifier.predict(payload.subject, payload.body)
    explanation = explain_status(label, confidence)
    db.add(RecruiterEmail(application_id=app.id, sender=str(payload.sender), subject=payload.subject, body=payload.body, classification=label, confidence=confidence))
    new_status = STATUS.get(label, app.status)
    update_status(db, app, new_status, explanation)
    create_notification(db, user.id, f"New recruiter communication detected for {app.company}: {label}.")
    return EmailAnalyzeResponse(classification=label, confidence=confidence, explanation=explanation, application_status=new_status)
