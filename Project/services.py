from datetime import date
from typing import Optional
from fastapi import HTTPException
from Project.repository import ProjectRepository
from Database.database import *
from Project.responses import (
    CreateProjectResponse,
    RemoveProjectResponse,
    UpdateProjectResponse,
)


project_instance = ProjectRepository()


def get_project_name(project_id: int) -> str:
    project = session.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project.name


def create_project(name: str, description: str, owner_id: int, start_date: date , end_date: Optional[date]=None):
    owner = session.query(User).filter(User.id == owner_id).first()
    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")

    new_project = project_instance.add(name, description, owner_id, start_date, end_date)
    return CreateProjectResponse(
        id=new_project.id,
        name=new_project.name,
        description=new_project.description,
        created_at=new_project.created_at,
        start_date=new_project.start_date,
        end_date=new_project.end_date
    )


def display_projects():  # method for main
    details = project_instance.get()
    return details


def remove_project(project_id):  # method for main
    delete_project = project_instance.remove(project_id)
    if not delete_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return RemoveProjectResponse(
        id=delete_project.id,
        name=delete_project.name,
        description=delete_project.description,
        created_at=delete_project.created_at,
        start_date=delete_project.start_date,
        end_date=delete_project.end_date
    )


def project_update(
    project_id: int, new_project_name: str, new_project_decription: str, start_date: date, end_date: Optional[date]=None
) -> UpdateProjectResponse:
    updated_project = project_instance.update(
        project_id, new_project_name, new_project_decription, start_date, end_date
    )
    if not updated_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return UpdateProjectResponse(
        id=updated_project.id,
        name=updated_project.name,
        description=updated_project.description,
        created_at=updated_project.created_at,
        start_date=updated_project.start_date,
        end_date=updated_project.start_date
    )

def display_project(project_id):
    details = project_instance.getproject(project_id)
    return details
