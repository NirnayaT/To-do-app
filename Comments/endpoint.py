from fastapi import APIRouter
from Comments.services import (
    display_comments,
    create_comment,
    remove_comment,
    update_comment as update_comment_route,
)
from Comments.payload import (
    CreateCommentPayload,
    RemoveCommentPayload,
    UpdateCommentPayload,
)
from fastapi import Depends
from Users.auth.jwt_bearer import jwtBearer

router = APIRouter()


@router.post("/comments/add", dependencies=[Depends(jwtBearer())])
async def add_comment(comment: CreateCommentPayload):
    return await create_comment(comment)


@router.get("/comments/show", dependencies=[Depends(jwtBearer())])
async def show_comments(task_id):
    return await display_comments(task_id)


@router.delete("/comments/remove", dependencies=[Depends(jwtBearer())])
async def delete_comment(payload: RemoveCommentPayload):
    return await remove_comment(payload), await display_comments(payload.task_id)


@router.put("/comments/update", dependencies=[Depends(jwtBearer())])
async def update_comment(payload: UpdateCommentPayload):
    return await update_comment_route(payload), await display_comments(payload.task_id)
