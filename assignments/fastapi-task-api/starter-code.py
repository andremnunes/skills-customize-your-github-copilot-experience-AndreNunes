from typing import Literal

from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Task API",
    description="An API for managing study tasks",
)


Priority = Literal["low", "medium", "high"]


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    priority: Priority = "medium"


class Task(TaskCreate):
    id: int
    completed: bool = False


# Keep the data in memory while the application is running.
tasks: list[Task] = [
    Task(
        id=1,
        title="Read the FastAPI documentation",
        description="Review path operations and automatic docs.",
        priority="medium",
    ),
    Task(
        id=2,
        title="Build the first endpoint",
        description="Create a GET endpoint that returns JSON.",
        priority="high",
        completed=True,
    ),
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks(
    completed: bool | None = Query(default=None),
    priority: Priority | None = Query(default=None),
):
    # TODO: filter the collection when query parameters are provided.
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: return the matching task or raise HTTPException with status 404.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    # TODO: create an ID, store the new task, and return it.
    raise NotImplementedError


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskCreate):
    # TODO: replace the matching task while preserving its ID and completion state.
    raise NotImplementedError


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    # TODO: remove the matching task or raise HTTPException with status 404.
    raise NotImplementedError
