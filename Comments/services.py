from fastapi import HTTPException
from tasks.services import get_task_name
from Comments.payload import (
    CreateCommentPayload,
    RemoveCommentPayload,
    UpdateCommentPayload,
)
from Comments.repository import CommentRepository
from Database.database import *
from Comments.responses import (
    CreateCommentResponse,
    RemoveCommentResponse,
    CommentResponse,
    UpdateCommentResponse,
)
from sockets.manager import manager

comment_instance = CommentRepository()


async def create_comment(comment_payload: CreateCommentPayload):
    new_comment = comment_instance.add(
        comment=comment_payload.comment,
        task_id=comment_payload.task_id,
        user_id=comment_payload.user_id,
    )
    task_name = get_task_name(comment_payload.task_id)
    response = CreateCommentResponse(
        id=new_comment.id,
        comment=new_comment.comment,
        created_on=new_comment.created_at,
        task_name=task_name,
    )
    await manager.broadcast(f"New comment added: {response.comment}")
    return response


async def remove_comment(payload: RemoveCommentPayload) -> RemoveCommentResponse:
    delete_comment = comment_instance.remove(payload.task_id, payload.comment_id)
    if not delete_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    task_name = get_task_name(payload.task_id)
    response = RemoveCommentResponse(
        id=delete_comment.id,
        comment=delete_comment.comment,
        created_on=delete_comment.created_at,
        task_name=task_name,
    )
    await manager.broadcast(f"Comment removed: {response.comment}")
    return response


async def update_comment(payload: UpdateCommentPayload) -> UpdateCommentResponse:
    updated_comment = comment_instance.update(
        payload.task_id, payload.comment_id, payload.new_comment
    )
    if not updated_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    task_name = get_task_name(payload.task_id)
    response = UpdateCommentResponse(
        id=updated_comment.id,
        new_comment=updated_comment.comment,
        created_on=updated_comment.created_at,
        task_name=task_name,
    )
    await manager.broadcast(f"Comment updated: {response.new_comment}")
    return response


async def display_comments(task_id):  # method for main
    details = comment_instance.get(task_id)
    task_name = get_task_name(task_id)
    response = [
        CommentResponse(
            id=comments.id,
            comment=comments.comment,
            created_on=comments.created_at,
            task_name=task_name,
        )
        for comments in details
    ]
    return {"Comments": response}
