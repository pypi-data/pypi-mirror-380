# !/usr/bin/env python3
"""日志类测试模块。

本模块提供以下核心功能:
- 测试日志类的基本功能
- 测试日志级别设置
- 测试日志文件输出
- 测试单例模式
"""
from __future__ import annotations

import os
import time

import pytest
from xtlog import LogCls, mylog
from xtlog.config import LOG_LEVELS


class TestLogCls:
    """测试日志类"""

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """在每个测试前后重置日志实例"""
        LogCls.reset_instance()
        yield
        LogCls.reset_instance()

    def test_singleton_pattern(self):
        """测试单例模式"""
        log1 = LogCls()
        log2 = LogCls()
        assert log1 is log2

    def test_log_levels(self):
        """测试日志级别设置"""
        for _level_name, level_value in LOG_LEVELS.items():
            LogCls.reset_instance()
            log = LogCls(level=level_value)
            assert log.current_level == level_value

    def test_file_output(self, tmp_path):
        """测试日志文件输出"""
        log_file = tmp_path / "test.log"
        log = LogCls(log_dir=str(tmp_path), log_file_name="test.log")
        log.info("测试日志文件输出")

        # 等待日志写入
        time.sleep(0.1)

        assert log_file.exists()
        with open(log_file, encoding="utf-8") as f:
            content = f.read()
            assert "测试日志文件输出" in content

    def test_global_instance(self):
        """测试全局日志实例"""
        mylog.info("测试全局日志实例")
        assert mylog is LogCls()

    def test_multiple_messages(self):
        """测试多条日志记录"""
        messages = ["消息1", "消息2", "消息3"]
        for msg in messages:
            mylog.info(msg)

        # 验证日志处理器是否正常工作
        assert len(mylog.loger._handlers) > 0

    def test_exception_logging(self):
        """测试异常日志记录"""
        try:
            1 / 0
        except Exception:
            mylog.exception("测试异常日志")

        # 验证异常处理器是否正常工作
        assert len(mylog.loger._handlers) > 0


class TestUtils:
    """测试工具函数"""

    def test_simplify_file_path(self):
        """测试简化文件路径函数"""
        from xtlog.utils import simplify_file_path

        test_path = os.path.abspath(__file__)
        simplified = simplify_file_path(test_path, 10, "test_function")

        assert "test_logger.py" in simplified
        assert "test_function" in simplified
        assert "10" in simplified
