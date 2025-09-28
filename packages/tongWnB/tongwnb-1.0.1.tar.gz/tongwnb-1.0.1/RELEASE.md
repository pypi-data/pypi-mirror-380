# TongWnB 发布流程

## 📦 重新打包发布步骤

### 1. 更新版本号

编辑 `tongWnB/package.json` 文件：

```json
{
  "name": "tongWnB",
  "version": "1.0.1",  // 更新版本号
  "description": "",
  "python": "true"
}
```

### 2. 清理和构建

```bash
# 激活虚拟环境
source venv/bin/activate

# 清理旧的构建文件
rm -rf dist/ build/

# 重新构建包
python -m build
```

### 3. 发布到PyPI

```bash
# 发布到PyPI（确保已配置TWINE_PASSWORD环境变量）
twine upload dist/*
```

## 🔄 完整命令

```bash
# 一键发布脚本
source venv/bin/activate && \
rm -rf dist/ build/ && \
python -m build && \
twine upload dist/*
```

## ✅ 验证发布

发布成功后，可以测试安装：

```bash
# 在新环境中测试安装
python -m venv test_env
source test_env/bin/activate
pip install tongwnb==新版本号
python -c "import tongWnB; print('安装成功!')"
deactivate
rm -rf test_env
```

## 📝 注意事项

- 确保版本号遵循语义化版本规范 (major.minor.patch)
- 发布前建议先在本地测试功能
- 每次发布后记得更新README中的版本信息
- 如果需要发布预览版本，可以使用 `1.0.1rc1` 等格式
