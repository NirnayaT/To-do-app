from enum import Enum
from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


class CreateProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    start_date: date
    end_date: Optional[date]=None


class RemoveProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    start_date: date
    end_date: Optional[date]=None


class UpdateProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    start_date: date
    end_date: Optional[date]=None

