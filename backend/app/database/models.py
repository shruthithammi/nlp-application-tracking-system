from datetime import datetime, timezone
from sqlalchemy import DateTime, ForeignKey, String, Text, Float, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.connection import Base

def now(): return datetime.now(timezone.utc)

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    applications: Mapped[list["Application"]] = relationship(back_populates="user", cascade="all, delete-orphan")

class Application(Base):
    __tablename__ = "applications"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    company: Mapped[str] = mapped_column(String(150))
    role: Mapped[str] = mapped_column(String(200))
    status: Mapped[str] = mapped_column(String(50), default="applied")
    applied_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)
    latest_explanation: Mapped[str | None] = mapped_column(Text, nullable=True)
    user: Mapped["User"] = relationship(back_populates="applications")
    events: Mapped[list["ApplicationEvent"]] = relationship(back_populates="application", cascade="all, delete-orphan")

class ApplicationEvent(Base):
    __tablename__ = "application_events"
    id: Mapped[int] = mapped_column(primary_key=True)
    application_id: Mapped[int] = mapped_column(ForeignKey("applications.id"), index=True)
    event_type: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)
    application: Mapped["Application"] = relationship(back_populates="events")

class RecruiterEmail(Base):
    __tablename__ = "recruiter_emails"
    id: Mapped[int] = mapped_column(primary_key=True)
    application_id: Mapped[int] = mapped_column(ForeignKey("applications.id"), index=True)
    sender: Mapped[str] = mapped_column(String(255))
    subject: Mapped[str] = mapped_column(String(500))
    body: Mapped[str] = mapped_column(Text)
    classification: Mapped[str] = mapped_column(String(50))
    confidence: Mapped[float] = mapped_column(Float, default=0.0)
    received_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)

class Notification(Base):
    __tablename__ = "notifications"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    message: Mapped[str] = mapped_column(Text)
    is_read: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)
