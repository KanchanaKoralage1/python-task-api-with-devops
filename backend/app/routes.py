from operator import index
from fastapi import APIRouter, HTTPException
from app.models import Task
from datetime import datetime

router=APIRouter()

tasks=[]

#create tasks
@router.post("/tasks")
def create_task(task: Task):
    task.created_at= datetime.now()
    tasks.append(task)
    return{
        "message":"Task created successfully",
        "task": task
    }


# get all task
@router.get("/tasks")
def get_tasks():
    return tasks


# get single task
@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="task not found")

# update tasks
@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task.created_at = task.created_at
            tasks[index]= updated_task
            return{
                "message":"Task updated successfully",
                "task":updated_task
            }
    raise HTTPException(status_code=404, detail="task not found")

#delete task
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id==task_id:
            tasks.pop(index)
            return{
                "message":"task deleted successfully",
            }
    raise HTTPException(status_code=404, detail="task not found")