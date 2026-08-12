from pydantic import BaseModel, EmailStr
class EmailAnalyzeRequest(BaseModel):
    application_id: int
    sender: EmailStr
    subject: str
    body: str
class EmailAnalyzeResponse(BaseModel):
    classification: str
    confidence: float
    explanation: str
    application_status: str
