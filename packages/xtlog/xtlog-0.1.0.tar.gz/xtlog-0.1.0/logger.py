# !/usr/bin/env python3
"""日志类模块。

本模块提供以下核心功能:
- 基于loguru的日志类实现
- 单例模式日志配置
- 文件和控制台双输出

主要特性:
- 线程安全的单例实现
- 自动日志文件轮转和保留
- 支持动态设置日志级别
- 开发环境智能检测

Author: sandorn sandorn@live.cn
Github: http://github.com/sandorn/xtlog
"""

from __future__ import annotations

import os
import sys
from collections.abc import Callable
from datetime import datetime
from threading import RLock
from weakref import WeakValueDictionary

from loguru import logger

from .config import OPTIMIZED_FORMAT
from .utils import format_record

# 是否为开发环境
IS_DEV: bool = os.getenv("ENV", "dev").lower() == "dev"


class SingletonMixin:
    """线程安全的单例混入类实现

    核心功能：
    - 通过混入方式实现单例模式
    - 支持与其他类的多重继承
    - 双重检查锁确保线程安全
    - 使用弱引用字典避免内存泄漏
    - 提供完整的实例管理接口

    类方法：
    - get_instance: 获取当前单例实例（不创建新实例）
    - reset_instance: 重置单例实例
    - has_instance: 检查是否存在单例实例

    类属性：
    - _instances: 弱引用字典，存储类与实例的映射关系
    - _instance_lock: 可重入锁，确保线程安全

    使用示例：
        # 基本用法
        class ConfigService(SingletonMixin):
            def __init__(self, config_file: str | None = None):
                print(f"加载配置文件: {config_file or '默认配置'}")
                self.config = config_file or 'default_config'

        # 创建实例
        config1 = ConfigService("app_config.json")
        config2 = ConfigService("user_config.json")

        # config1和config2是同一个实例
        print(f"是同一个实例: {config1 is config2}")  # 输出: True
        print(f"配置文件: {config1.config}")  # 输出: app_config.json

        # 实例管理
        print(f"存在实例: {ConfigService.has_instance()}")  # 输出: True

        # 重置实例
        ConfigService.reset_instance()

        # 重置后创建新实例
        config3 = ConfigService("new_config.json")
        print(f"新配置文件: {config3.config}")  # 输出: new_config.json

        # 多重继承示例
        class Loggable:
            def log(self, message: str) -> None:
                print(f"[LOG] {message}")

        class LoggedConfigService(ConfigService, Loggable):
            pass

        logged_config = LoggedConfigService("logged_config.json")
        logged_config.log(f"当前配置: {logged_config.config}")
    """

    _instance_lock: RLock = RLock()  # 使用可重入锁，避免递归调用问题
    _instances: WeakValueDictionary[type, SingletonMixin] = WeakValueDictionary()

    def __new__(cls: type[SingletonMixin], *args: object, **kwargs: object) -> SingletonMixin:
        """实例化处理（带错误日志和双重检查锁）"""
        # 第一次检查（无锁）
        if cls in cls._instances:
            return cls._instances[cls]

        # 获取锁
        with cls._instance_lock:
            # 第二次检查（有锁）
            if cls in cls._instances:
                return cls._instances[cls]

            try:
                # 创建实例
                instance = super().__new__(cls)
                # 存储实例引用
                cls._instances[cls] = instance
                # 注意：不手动调用__init__，让Python正常流程处理初始化
                return instance
            except Exception as e:
                # 清理失败的实例
                if cls in cls._instances:
                    del cls._instances[cls]
                # 改进错误处理，记录异常并重新抛出
                raise RuntimeError(f"SingletonMixin {cls.__name__} __new__ failed: {e}") from e

    @classmethod
    def reset_instance(cls: type[SingletonMixin]) -> None:
        """重置单例实例"""
        with cls._instance_lock:
            cls._instances.pop(cls, None)  # 移除该类的实例引用

    @classmethod
    def has_instance(cls: type[SingletonMixin]) -> bool:
        """检查是否存在单例实例"""
        return cls in cls._instances

    @classmethod
    def get_instance(cls: type[SingletonMixin]) -> SingletonMixin | None:
        """获取当前单例实例（不创建新实例）"""
        return cls._instances.get(cls) if cls in cls._instances else None


class LogCls(SingletonMixin):
    """
    简化版日志配置类 - 利用loguru的record对象获取调用信息

    特性：
    - 单例模式，确保全局只有一个日志实例
    - 支持文件和控制台双输出
    - 自动处理日志文件轮转和保留
    - 支持callfrom参数扩展功能

    Attributes:
        DEFAULT_LOG_LEVEL: 默认日志级别
        current_level: 当前日志级别
        log_file: 日志文件路径
        log_file_rotation_size: 日志文件轮转大小
        log_file_retention_days: 日志文件保留天数
        log_format: 日志格式
    """

    # 默认日志级别
    DEFAULT_LOG_LEVEL: int = 10  # DEBUG级别

    def __init__(
        self,
        level: int = 10,  # DEBUG级别
        serialize: bool = False,
        log_file_rotation_size: str = "16 MB",
        log_file_retention_days: str = "30 days",
        log_format: str = OPTIMIZED_FORMAT,
    ) -> None:
        """
        初始化日志配置

        Args:
            level: 日志级别，默认为10(DEBUG级别)
            serialize: 是否序列化日志，默认为False
            log_file_rotation_size: 日志文件轮转大小，默认为16 MB
            log_file_retention_days: 日志文件保留天数，默认为30天
            log_format: 日志格式，默认为优化的格式
        """
        self.loger = logger
        self.loger.remove()

        # 应用格式处理
        self.loger = self.loger.patch(format_record)

        # 设置工作目录和日志文件
        workspace_root: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logs_dir: str = os.path.join(workspace_root, "logs")
        os.makedirs(logs_dir, exist_ok=True)
        log_file: str = os.path.join(logs_dir, f"xt_{datetime.now().strftime('%Y%m%d')}.log")

        # 保存配置信息
        self.current_level = level
        self.log_file = log_file
        self._file_id = None
        self._console_id = None

        # 保存参数到实例变量
        self.log_file_rotation_size = log_file_rotation_size
        self.log_file_retention_days = log_file_retention_days
        self.log_format = log_format

        # 文件日志配置
        self._file_id = self.loger.add(
            log_file,
            rotation=log_file_rotation_size,
            retention=log_file_retention_days,
            level=level,
            encoding="utf-8",
            format=log_format,
            serialize=serialize,
            backtrace=True,
            diagnose=True,
            catch=True,
        )

        # 控制台日志配置（仅开发环境）
        if IS_DEV:
            self._console_id = self.loger.add(
                sys.stderr,
                level=level,
                format=log_format,
                serialize=serialize,
                backtrace=True,
                diagnose=True,
                catch=True,
            )

    def __call__(self, *args: object, **kwargs: object) -> list[None]:
        """
        支持实例直接调用，将多个参数作为多条日志记录

        Args:
            *args: 要记录的参数
            **kwargs: 传递给loguru的额外参数

        Returns:
            list[None]: 每条日志的记录结果列表
        """
        return [self.loger.info(arg, **kwargs) for arg in args]

    def __getattr__(self, attr: str) -> Callable[..., None]:
        """
        动态获取属性，支持直接调用loguru的方法

        Args:
            attr: 属性名

        Returns:
            Callable[..., None]: loguru的对应方法或默认日志函数
        """
        def fallback_log(*arg: object, **kwargs: object) -> None:
            """默认的日志函数，用于处理不存在的日志方法"""
            self.loger.info(*arg, **kwargs)
        try:
            method = getattr(self.loger, attr)
            if callable(method):
                # 使用类型转换确保返回类型正确
                return method  # type: ignore[no-any-return]
            else:
                # 如果属性不是可调用的，返回一个默认的日志函数
                return fallback_log
        except AttributeError:
            # 如果属性不存在，返回一个默认的日志函数
            return fallback_log

    def set_level(self, level: int | str) -> None:
        """
        动态设置日志级别

        Args:
            level: 日志级别，可以是整数或字符串

        Example:
            >>> mylog.set_level("DEBUG")  # 设置为DEBUG级别
            >>> mylog.set_level(30)       # 设置为WARNING级别
        """
        from .config import LOG_LEVELS

        # 转换字符串级别为整数
        if isinstance(level, str):
            level = LOG_LEVELS.get(level.upper(), self.DEFAULT_LOG_LEVEL)

        self.current_level = level

        # 使用正确的方法更新日志级别
        if self._file_id is not None:
            self.loger.remove(self._file_id)
            self._file_id = self.loger.add(
                self.log_file,
                rotation=self.log_file_rotation_size,
                retention=self.log_file_retention_days,
                level=level,
                encoding="utf-8",
                format=self.log_format,
                serialize=False,
                backtrace=True,
                diagnose=True,
                catch=True,
            )

        if self._console_id is not None:
            self.loger.remove(self._console_id)
            self._console_id = self.loger.add(
                sys.stderr,
                level=level,
                format=self.log_format,
                serialize=False,
                backtrace=True,
                diagnose=True,
                catch=True,
            )
