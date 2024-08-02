from fastapi import APIRouter
from Project.services import (
    display_projects,
    create_project,
    remove_project,
    project_update,
    display_project,
)
from Project.payload import (
    CreateProjectPayload,
    RemoveProjectPayload,
    UpdateProjectPayload,
)
from fastapi import Depends
from Users.auth.jwt_bearer import jwtBearer

router = APIRouter()


@router.post("/projects/add", dependencies=[Depends(jwtBearer())])
def add_project(payload: CreateProjectPayload):
    return (
        create_project(
            payload.project_name,
            payload.project_description,
            payload.owner_id,
            payload.start_date,
            payload.end_date,
        ),
        display_projects(),
    )


@router.get("/projects/show", dependencies=[Depends(jwtBearer())])
def show_projects():
    return display_projects()


@router.put("/projects/update", dependencies=[Depends(jwtBearer())])
def update_project(payload: UpdateProjectPayload):
    return (
        project_update(
            payload.project_id,
            payload.new_project_name,
            payload.new_project_description,
            payload.start_date,
            payload.end_date
        ),
        display_projects(),
    )


@router.delete("/projects/remove", dependencies=[Depends(jwtBearer())])
def delete_project(payload: RemoveProjectPayload):
    return remove_project(payload.project_id), display_projects()


@router.get("/projects/project/show", dependencies=[Depends(jwtBearer())])
def get_project(project_id):
    return display_project(project_id)
