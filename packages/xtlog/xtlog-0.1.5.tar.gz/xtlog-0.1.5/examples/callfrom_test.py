# !/usr/bin/env python3
"""callfrom参数测试示例。

本示例专门测试在不同日志级别设置下callfrom参数的表现。

Author: sandorn sandorn@live.cn
Github: http://github.com/sandorn/xtlog
"""
from __future__ import annotations

import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# 导入xtlog
from xtlog import mylog


def test_function(level: str, *args, **kwargs):
    """测试函数，用于演示callfrom参数在不同日志级别下的表现"""
    mylog.info("测试{}级别 - args:{} kw:{}", level, args, kwargs, callfrom=test_function)
    mylog.debug("测试{}级别 - debug信息", level, callfrom=test_function)
    mylog.warning("测试{}级别 - warning信息", level, callfrom=test_function)
    mylog.error("测试{}级别 - error信息", level, callfrom=test_function)


def main():
    """主函数，测试callfrom参数在不同日志级别下的表现"""
    print("=== 测试callfrom参数在不同日志级别下的表现 ===\n")
    
    # 初始测试 (默认DEBUG级别)
    print("1. 初始状态 (DEBUG级别):")
    test_function("DEBUG", 1, 2, 3, name="initial")
    
    # 设置为INFO级别
    print("\n2. 设置为INFO级别:")
    mylog.set_level("INFO")
    test_function("INFO", 4, 5, 6, name="info_test")
    
    # 设置为WARNING级别
    print("\n3. 设置为WARNING级别:")
    mylog.set_level("WARNING")
    test_function("WARNING", 7, 8, 9, name="warning_test")
    
    # 设置为ERROR级别
    print("\n4. 设置为ERROR级别:")
    mylog.set_level("ERROR")
    test_function("ERROR", 10, 11, 12, name="error_test")
    
    # 设置为DEBUG级别
    print("\n5. 设置为DEBUG级别:")
    mylog.set_level("DEBUG")
    test_function("DEBUG", 13, 14, 15, name="final_test")


if __name__ == "__main__":
    main()