"""Workflow engine."""

from typing import List, Callable
from .task import Task

class Workflow:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []
    
    def add_task(self, task: Task):
        self.tasks.append(task)
    
    def run(self):
        for task in self.tasks:
            task.execute()
