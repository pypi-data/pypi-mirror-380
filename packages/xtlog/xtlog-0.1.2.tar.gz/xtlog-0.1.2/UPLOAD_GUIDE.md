# PyPI 上传指南

## 包信息
- 包名: `xtlog`
- 版本: `0.1.1`
- 描述: 基于loguru的高性能日志库

## 构建的包文件
- `dist/xtlog-0.1.1-py3-none-any.whl` - Wheel包
- `dist/xtlog-0.1.1.tar.gz` - 源码包

## 上传到PyPI

### 1. 测试上传（TestPyPI）
```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

### 2. 正式上传（PyPI）
```bash
twine upload dist/*
```

### 3. 使用API token上传（推荐）
```bash
twine upload -u __token__ -p your-api-token dist/*
```

## 安装测试
```bash
# 从TestPyPI安装测试
pip install -i https://test.pypi.org/simple/ xtlog

# 从正式PyPI安装
pip install xtlog
```

## 包结构验证
```bash
# 检查包文件
twine check dist/*

# 测试安装
pip install dist/xtlog-0.1.1-py3-none-any.whl

# 验证导入
python -c "import xtlog; print(f'版本: {xtlog.__version__}')"
```

## 包内容
- `xtlog/__init__.py` - 主模块入口
- `xtlog/logger.py` - 日志类实现
- `xtlog/config.py` - 配置模块
- `xtlog/utils.py` - 工具函数

## 依赖项
- `loguru>=0.7.0`

## 兼容性
- Python >= 3.10
- 跨平台支持（Windows/Linux/macOS）

## 发布检查清单
- [x] 版本号已更新到 0.1.1
- [x] README.md 内容完整
- [x] pyproject.toml 配置正确
- [x] 包构建成功
- [x] twine 检查通过
- [x] 本地安装测试通过
- [x] 导入功能验证通过

## 下一步
1. 配置PyPI账户和API token
2. 执行上传命令
3. 验证包在PyPI上的显示
4. 更新文档和示例