from datetime import datetime
from pydantic import BaseModel, ConfigDict
class ApplicationCreate(BaseModel):
    company: str
    role: str
    applied_date: datetime | None = None
class ApplicationUpdate(BaseModel):
    status: str | None = None
    latest_explanation: str | None = None
class EventOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    event_type: str
    description: str
    created_at: datetime
class ApplicationOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    company: str
    role: str
    status: str
    applied_date: datetime
    latest_explanation: str | None
    events: list[EventOut] = []
