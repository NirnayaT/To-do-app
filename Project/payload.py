from typing import Optional
from pydantic import BaseModel
from datetime import date

class CreateProjectPayload(BaseModel):
    project_name: str
    project_description: str
    owner_id: int
    start_date: date
    end_date: Optional[date]=None


class RemoveProjectPayload(BaseModel):
    project_id: int


class UpdateProjectPayload(BaseModel):
    project_id: int
    new_project_name: str
    new_project_description: str
    start_date: date
    end_date: Optional[date]=None
