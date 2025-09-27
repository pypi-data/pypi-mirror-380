"""
基础类类型提示
"""

from typing import Any, Self, TypeVar

T = TypeVar('T')

class Base:
    """
    操作结果处理的基础类
    """
    
    ret: Any
    bool: bool
    text: str
    
    def __init__(self) -> None: ...
    def value(self) -> Any: ...
    def user_login(self) -> None: ...
    def execute_function(self) -> None: ...