from sqlalchemy.orm import Session
from app.database.models import Application, ApplicationEvent

def create_application(db: Session, user_id: int, company: str, role: str, applied_date):
    app = Application(user_id=user_id, company=company, role=role, applied_date=applied_date,
                      status="applied", latest_explanation="Your application has been recorded. No recruiter update has been detected yet.")
    db.add(app); db.flush()
    db.add(ApplicationEvent(application_id=app.id, event_type="applied", description="Application recorded by the candidate."))
    db.commit(); db.refresh(app); return app

def update_status(db: Session, app: Application, status: str, explanation: str):
    app.status = status; app.latest_explanation = explanation
    db.add(ApplicationEvent(application_id=app.id, event_type=status, description=explanation))
    db.commit(); db.refresh(app); return app
