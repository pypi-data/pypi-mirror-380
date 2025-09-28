# !/usr/bin/env python3
"""日志配置模块。

本模块提供以下核心功能:
- 日志级别映射定义
- 日志图标配置
- 日志格式设置

主要特性:
- 统一的日志级别管理
- 丰富的日志图标支持
- 优化的日志格式模板

Author: sandorn sandorn@live.cn
Github: http://github.com/sandorn/xtlog
"""

from __future__ import annotations

# 日志级别映射
LOG_LEVELS: dict[str, int] = {"TRACE": 5, "DEBUG": 10, "INFO": 20, "SUCCESS": 25, "WARNING": 30, "ERROR": 40, "CRITICAL": 50}


# 日志图标
LOG_ICONS: dict[str, str] = {
    "TRACE": "\u270f\ufe0f",  # ✏️ - 跟踪日志
    "START": "\u25b6\ufe0f",  # ▶️ - 开始执行
    "STOP": "\u23f9\ufe0f",  # ⏹️ - 停止执行
    "DEBUG": "\U0001f41e",  # 🐞 - 调试信息
    "INFO": "\u2139\ufe0f",  # ℹ️ - 普通信息
    "SUCCESS": "\u2705\ufe0f",  # ✅ - 成功信息
    "WARNING": "\u26a0\ufe0f",  # ⚠️ - 警告信息
    "ERROR": "\u274c\ufe0f",  # ❌ - 错误信息
    "CRITICAL": "\u2620\ufe0f",  # ☠️ - 严重错误
    "DENIED": "\u26d4\ufe0f",  # ⛔ - 拒绝操作
}


# 日志格式
OPTIMIZED_FORMAT: str = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> <level>{level.icon}</level> | "
    "<magenta>{process: >6}</magenta>:<yellow>{thread: <6}</yellow> | "
    "<cyan>{extra[simplified_path]: <35}</cyan> | "
    "<level>{message}</level>"
)
