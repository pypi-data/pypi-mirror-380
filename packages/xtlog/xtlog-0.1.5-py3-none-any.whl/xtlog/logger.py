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
- 支持自定义日志路径和文件名

Author: sandorn sandorn@live.cn
Github: http://github.com/sandorn/xtlog
"""

from __future__ import annotations

from collections.abc import Callable
from datetime import datetime
import os
import sys
from threading import RLock
from typing import Self
from weakref import WeakValueDictionary

from loguru import logger

from .config import LOG_LEVELS, OPTIMIZED_FORMAT
from .utils import format_record

# 是否为开发环境
IS_DEV: bool = os.getenv('ENV', 'dev').lower() == 'dev'


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
    _instances: WeakValueDictionary[type, Self] = WeakValueDictionary()

    def __new__(
        cls: type[Self],
        level: int | str = 10,
        serialize: bool = False,
        log_file_rotation_size: str = '16 MB',
        log_file_retention_days: str = '30 days',
        log_format: str = OPTIMIZED_FORMAT,
        log_dir: str | None = None,
        log_file_name: str | None = None,
    ) -> Self:
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
                raise RuntimeError(f'SingletonMixin {cls.__name__} __new__ failed: {e}') from e

    @classmethod
    def reset_instance(cls: type[Self]) -> None:
        """重置单例实例"""
        with cls._instance_lock:
            _ = cls._instances.pop(cls, None)  # 移除该类的实例引用

    @classmethod
    def has_instance(cls: type[Self]) -> bool:
        """检查是否存在单例实例"""
        return cls in cls._instances

    @classmethod
    def get_instance(cls: type[Self]) -> Self | None:
        """获取当前单例实例（不创建新实例）"""
        return cls._instances.get(cls) if cls in cls._instances else None


class LogCls(SingletonMixin):
    # 默认日志级别
    DEFAULT_LOG_LEVEL: int = 10  # DEBUG级别

    def __init__(
        self,
        level: int | str = 10,
        serialize: bool = False,
        log_file_rotation_size: str = '16 MB',
        log_file_retention_days: str = '30 days',
        log_format: str = OPTIMIZED_FORMAT,
        log_dir: str | None = None,
        log_file_name: str | None = None,
    ) -> None:
        # 首先配置基础logger
        self.loger = logger.bind()
        self.loger.remove()

        # 应用patch在所有handler添加前
        self.loger = self.loger.patch(format_record)  # pyright: ignore[reportArgumentType]

        # 转换字符串级别为整数
        if isinstance(level, str):
            level = LOG_LEVELS.get(level.upper(), self.DEFAULT_LOG_LEVEL)

        # 设置工作目录和日志文件
        if log_dir is None:
            try:
                workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            except Exception:
                workspace_root = os.getcwd()

            logs_dir = os.path.join(workspace_root, 'logs')
        else:
            logs_dir = os.path.abspath(log_dir)

        os.makedirs(logs_dir, exist_ok=True)

        if log_file_name is None:
            log_file_name = f'xt_{datetime.now().strftime("%Y%m%d")}.log'

        log_file = os.path.join(logs_dir, log_file_name)

        # 保存配置信息
        self.log_format = log_format
        self.current_level = level
        self.log_file = log_file
        self.serialize = serialize
        self.log_file_rotation_size = log_file_rotation_size
        self.log_file_retention_days = log_file_retention_days

        self._file_id = None
        self._console_id = None
        # 重新设计handler添加方法，确保patch效果不被破坏
        self._setup_handlers()

    def _setup_handlers(self) -> None:
        """统一设置handlers，确保patch效果一致"""
        # 清理现有handlers
        if self._file_id is not None:
            self.loger.remove(self._file_id)
        if self._console_id is not None:
            self.loger.remove(self._console_id)

        # 文件日志配置 - 使用patch后的logger
        self._file_id = self.loger.add(
            self.log_file,
            rotation=self.log_file_rotation_size,
            retention=self.log_file_retention_days,
            level=self.current_level,
            encoding='utf-8',
            format=self.log_format,
            serialize=self.serialize,
            backtrace=True,
            diagnose=True,
            catch=True,
        )

        # 控制台日志配置（仅开发环境）
        if IS_DEV:
            self._console_id = self.loger.add(
                sys.stderr,
                level=self.current_level,
                format=self.log_format,
                serialize=self.serialize,
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

    def __getattr__(self, attr: str) -> Callable[..., object]:
        """
        动态获取属性，支持直接调用loguru的方法

        Args:
            attr: 属性名

        Returns:
            Callable[..., object]: loguru的对应方法或默认日志函数
        """

        try:
            return getattr(self.loger, attr)
        except AttributeError as e:
            raise AttributeError(f"'LogCls' object has no attribute '{attr}'") from e

    def set_level(self, level: int | str) -> None:
        """动态设置日志级别"""
        from .config import LOG_LEVELS

        if isinstance(level, str):
            level = LOG_LEVELS.get(level.upper(), self.DEFAULT_LOG_LEVEL)

        self.current_level = level
        # 重新设置handlers，保持patch
        self._setup_handlers()

    def get_logger(self):
        """
        获取原始的loguru logger实例

        Returns:
            Logger: loguru的logger实例
        """
        return self.loger
