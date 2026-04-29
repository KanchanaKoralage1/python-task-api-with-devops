from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    priority: Priority = Priority.medium
    created_at: datetime = datetime.now()
    due_date: Optional[datetime] = None