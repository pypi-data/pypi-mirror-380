# !/usr/bin/env python3
"""xtlog基本用法示例。

本示例展示了xtlog库的基本用法，包括：
- 基本日志记录
- 不同日志级别的使用
- 自定义日志配置
- callfrom参数的使用

Author: sandorn sandorn@live.cn
Github: http://github.com/sandorn/xtlog
"""

import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# 导入xtlog
from xtlog import mylog


def example_function():
    """示例函数，用于演示callfrom参数"""
    # 使用callfrom参数，指定日志来源为当前函数
    mylog.info("这条日志来自example_function", callfrom=example_function)

    # 不使用callfrom参数
    mylog.info("这条日志没有使用callfrom参数")


def main():
    """主函数，演示xtlog的基本用法"""
    # 1. 使用全局日志实例
    mylog.info("这是一条信息日志")
    mylog.debug("这是一条调试日志")
    mylog.warning("这是一条警告日志")
    mylog.error("这是一条错误日志")
    mylog.critical("这是一条严重错误日志")

    # 2. 直接调用日志实例
    mylog("这是直接调用的第一条日志", "这是直接调用的第二条日志")

    # 3. 设置日志级别
    print("\n设置日志级别为WARNING...\n")
    mylog.set_level("WARNING")
    mylog.debug("这条调试日志不会显示")
    mylog.info("这条信息日志不会显示")
    mylog.warning("这条警告日志会显示")

    # 4. 使用callfrom参数
    print("\n使用callfrom参数...\n")
    example_function()


if __name__ == "__main__":
    main()
