"""Task abstraction."""

from typing import Callable, Any

class Task:
    def __init__(self, name: str, func: Callable = None):
        self.name = name
        self.func = func
    
    def execute(self, **kwargs) -> Any:
        if self.func:
            return self.func(**kwargs)
        raise NotImplementedError
