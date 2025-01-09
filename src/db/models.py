from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import declarative_base, relationship
import enum
from datetime import datetime

# Base class for all models
Base = declarative_base()

# Enum for task status
class TaskStatus(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"

# Users table
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), nullable=False, unique=True)
    is_admin = Column(Boolean, default=False)

    # Relationships
    tasks = relationship("Task", back_populates="assigned_user")

# Tasks table
class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, index=True)
    assigned_user_id = Column(Integer, ForeignKey("users.user_id"))
    task_description = Column(String(1024), nullable=False)
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDING)  # Use TaskStatus enum
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    assigned_user = relationship("User", back_populates="tasks")
