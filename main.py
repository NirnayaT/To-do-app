from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from tasks.endpoint import router as tasks_endpoint_router
from Users.endpoint import router as users_endpoint_router
from Project.endpoint import router as projects_endpoint_router
from Comments.endpoint import router as comments_endpoint_router
from sockets.handler import router as sockets_router
from htmlexample import html

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def main():
    return HTMLResponse(html)  # {"Welcome": "to Project Management App."}


app.include_router(users_endpoint_router)
app.include_router(projects_endpoint_router)
app.include_router(tasks_endpoint_router)
app.include_router(comments_endpoint_router)
app.include_router(sockets_router)
