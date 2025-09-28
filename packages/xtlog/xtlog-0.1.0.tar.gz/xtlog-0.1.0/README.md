# xtlog

基于 loguru 的高性能日志库

## 特性

- 🚀 **高性能**: 基于 loguru 的高性能日志记录
- 📝 **双输出**: 文件和控制台双输出支持
- 🔄 **自动轮转**: 自动日志文件轮转和保留
- 🎯 **单例模式**: 确保全局只有一个日志实例
- 📍 **智能定位**: 自动识别调用位置信息
- ⚙️ **动态配置**: 支持动态设置日志级别
- 🎨 **丰富图标**: 支持丰富的日志图标显示

## 安装

```bash
pip install xtlog
```

## 快速开始

```python
from xtlog import mylog

# 基本使用
mylog.info("这是一条信息日志")
mylog.error("这是一条错误日志")

# 支持直接调用
mylog("第一条日志", "第二条日志")

# 设置日志级别
mylog.set_level("DEBUG")
```

## 高级功能

### 自定义日志配置

```python
from xtlog import LogCls

# 创建自定义日志实例
custom_log = LogCls(
    level=20,  # INFO级别
    log_file_rotation_size="10 MB",
    log_file_retention_days="7 days"
)

custom_log.info("自定义配置的日志")
```

### 使用 callfrom 参数

```python
from xtlog import mylog

def my_function():
    mylog.info("函数内的日志", callfrom=my_function)

my_function()
```

## 日志级别

支持以下日志级别：

- `TRACE` (5)
- `DEBUG` (10)
- `INFO` (20)
- `SUCCESS` (25)
- `WARNING` (30)
- `ERROR` (40)
- `CRITICAL` (50)

## 配置

### 环境变量

- `ENV`: 设置环境类型，`dev` 为开发环境（显示控制台日志），其他为生产环境

### 默认配置

- 日志文件位置: `项目根目录/logs/xt_YYYYMMDD.log`
- 文件轮转大小: `16 MB`
- 文件保留天数: `30 days`
- 默认日志级别: `DEBUG` (10)

## 开发

### 安装开发依赖

```bash
pip install -e .[dev]
```

### 代码检查

```bash
ruff check --fix --unsafe-fixes
```

### 类型检查

```bash
mypy .
```

## 许可证

MIT License

## 作者

sandorn <sandorn@live.cn>

GitHub: [http://github.com/sandorn/xtlog](http://github.com/sandorn/xtlog)