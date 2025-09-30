# !/usr/bin/env python3
"""日志工具函数模块。

本模块提供以下核心功能:
- 函数位置信息获取
- 文件路径简化处理
- 日志记录格式化

主要特性:
- 自动识别函数调用位置
- 智能路径简化算法
- 支持callfrom参数扩展
- 跨平台路径处理

Author: sandorn sandorn@live.cn
Github: http://github.com/sandorn/xtlog
"""

from __future__ import annotations

from collections.abc import Callable
import contextlib
import inspect
import os
from typing import Any


def get_function_location(func: Callable[..., object]) -> dict[str, str | int]:
    """
    获取函数的位置信息（文件、行号、函数名）

    Args:
        func: 要获取位置信息的函数

    Returns:
        dict: 包含文件路径、行号和函数名的字典

    Example:
        >>> location = get_function_location(some_function)
        >>> print(location)
        {'file': '/path/to/file.py', 'line': 10, 'function': 'some_function'}
    """
    # 基础检查
    if not callable(func):
        return {"file": "unknown", "line": 0, "function": "unknown"}

    # 获取原始函数（处理装饰器情况）
    original_func: Callable[..., object] = func

    # 使用inspect模块获取原始函数
    if hasattr(inspect, "unwrap"):
        with contextlib.suppress(Exception):
            original_func = inspect.unwrap(func)

    # 尝试使用__code__属性获取位置信息（最可靠的方法）
    if hasattr(original_func, "__code__"):
        code = original_func.__code__
        return {"file": code.co_filename, "line": code.co_firstlineno, "function": original_func.__name__}

    # 回退方案：使用inspect.getfile
    try:
        file_path = inspect.getfile(original_func)
        _source_lines, line_no = inspect.getsourcelines(original_func)
        return {"file": file_path, "line": line_no, "function": original_func.__name__}
    except Exception:
        # 最后的回退方案
        return {"file": getattr(func, "__module__", "unknown"), "line": 0, "function": getattr(func, "__name__", "unknown")}


def simplify_file_path(file_path: str, line_no: int, func_name: str) -> str:
    """
    简化文件路径，提取有意义的模块信息

    支持跨平台路径处理，确保在Windows和Unix系统上都能正确工作

    Args:
        file_path: 原始文件路径
        line_no: 行号
        func_name: 函数名

    Returns:
        str: 简化后的路径格式（如：module.file:line@function）

    Example:
        >>> path = simplify_file_path('/project/src/module/file.py', 10, 'test_func')
        >>> print(path)  # 输出: module.file:10@test_func
    """
    # 基础检查
    if not file_path or file_path == "unknown":
        return f"unknown:{line_no}@{func_name}"

    try:
        # 标准化路径
        file_path = os.path.normpath(file_path)

        # 获取项目根目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(current_dir))
        project_root = os.path.normpath(project_root)

        # 检查文件路径是否在项目根目录下
        try:
            common_path = os.path.commonpath([project_root, file_path])
            is_in_project = common_path == project_root
        except ValueError:
            is_in_project = False

        # 转换为相对路径或保持绝对路径
        relative_path = os.path.relpath(file_path, project_root) if is_in_project else file_path

        # 分解路径并提取有意义的部分
        parts = []
        path_temp = relative_path
        while path_temp and path_temp != os.path.sep:
            path_temp, part = os.path.split(path_temp)
            if part:
                parts.insert(0, part)

        if not parts:
            return f"unknown:{line_no}@{func_name}"

        # 提取文件名和模块路径
        filename = os.path.splitext(parts[-1])[0]

        # 构建模块路径（最多显示2级目录）
        if len(parts) > 1:
            # 取最后2级目录
            module_parts = parts[-3:-1] if len(parts) >= 3 else parts[:-1]
            module_path = ".".join(module_parts[-2:])  # 最多显示2级目录
            if module_path:
                return f"{module_path}.{filename}:{line_no}@{func_name}"

        return f"{filename}:{line_no}@{func_name}"

    except Exception:
        # 简化错误处理
        try:
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            return f"{base_name}:{line_no}@{func_name}"
        except Exception:
            return f"unknown:{line_no}@{func_name}"


def format_record(record: dict[str, Any]) -> None:
    """
    格式化日志记录，处理callfrom参数

    这个函数作为loguru的record处理器，负责：
    1. 检查是否有callfrom参数
    2. 根据callfrom参数或默认信息生成简化路径
    3. 设置simplified_path到record的extra中
    4. 清理 callfrom 参数避免格式化冲突

    Args:
        record: loguru的日志记录字典

    Note:
        callfrom参数用于指定日志的调用来源，可以覆盖默认的调用栈信息
    """
    # 确保extra字典存在（使用字典的get方法）
    record["extra"] = record.get("extra", {})

    try:
        # 检查是否有callfrom参数
        callfrom = record["extra"].get("callfrom")

        if callfrom is not None:
            # 验证callfrom参数类型
            if not callable(callfrom):
                raise TypeError("callfrom参数必须是可调用对象")

            # 获取位置信息
            location = get_function_location(callfrom)
            file_path = str(location["file"])
            line_no = int(location["line"])
            func_name = str(location["function"])

            # 生成简化路径
            simplified_path = simplify_file_path(file_path, line_no, func_name)
            record["extra"]["simplified_path"] = simplified_path

            # 清理callfrom参数
            if "callfrom" in record["extra"]:
                del record["extra"]["callfrom"]

        else:
            # 使用默认的调用位置信息
            try:
                # 从record字典中获取文件、行号和函数名信息
                default_file_path = record["file"].get("path", "unknown") if isinstance(record.get("file"), dict) else str(record.get("file", "unknown"))

                default_line_no = record.get("line", 0)
                default_func_name = record.get("function", "unknown")

                default_simplified_path = simplify_file_path(default_file_path, default_line_no, default_func_name)
                record["extra"]["simplified_path"] = default_simplified_path
            except Exception:
                record["extra"]["simplified_path"] = "unknown:0@unknown"

    except Exception:
        # 错误处理：设置默认值
        record["extra"]["simplified_path"] = "unknown:0@unknown"
