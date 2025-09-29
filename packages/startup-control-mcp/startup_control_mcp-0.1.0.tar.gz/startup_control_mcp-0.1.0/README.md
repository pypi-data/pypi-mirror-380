# Startup Control MCP | 开机启动项控制

[![PyPI Version](https://img.shields.io/pypi/v/startup-control-mcp.svg)](https://pypi.org/project/startup-control-mcp/)
[![Python Support](https://img.shields.io/pypi/pyversions/startup-control-mcp.svg)](https://pypi.org/project/startup-control-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://img.shields.io/pypi/dm/startup-control-mcp.svg)](https://pypi.org/project/startup-control-mcp/)

一个强大的跨平台开机启动项管理工具，支持智能分析、自然语言交互和安全管理。

A powerful cross-platform startup item management tool with intelligent analysis, natural language interaction, and secure management.

## ✨ 核心功能

### 🔍 智能启动项管理
- **跨平台支持**: Windows、macOS、Linux 全平台兼容
- **全面扫描**: 注册表、启动文件夹、LaunchAgents、systemd 等
- **智能分类**: 自动识别关键启动项和可优化项目
- **安全保护**: 防止误禁用系统关键启动项

### 🗣️ 自然语言交互
- **中文支持**: 完全支持中文自然语言命令
- **智能匹配**: 根据描述自动匹配相关启动项
- **批量操作**: 一句话控制多个相关启动项

### 📊 性能分析
- **启动时间优化**: 分析启动项对系统性能的影响
- **个性化建议**: 基于使用习惯提供优化建议
- **数据统计**: 详细的启动项统计信息

### 🛡️ 安全功能
- **自动备份**: 操作前自动备份当前状态
- **一键恢复**: 支持从备份恢复启动项配置
- **安全检查**: 智能识别并保护关键系统启动项

## 📦 安装 | Installation

### 从 PyPI 安装 | Install from PyPI
```bash
pip install startup-control-mcp
```

### 从源码安装 | Install from Source
```bash
git clone https://github.com/yourusername/startup-control-mcp.git
cd startup-control-mcp
pip install -e .
```

### 配置MCP服务器 | Configure MCP Server

#### 方法1: 作为Python模块运行（推荐）
```json
{
  "mcpServers": {
    "startup-control": {
      "command": "python",
      "args": ["-m", "startup_control_mcp.server"],
      "env": {}
    }
  }
}
```

#### 方法2: 使用命令行工具
```json
{
  "mcpServers": {
    "startup-control": {
      "command": "startup-control-mcp",
      "args": [],
      "env": {}
    }
  }
}
```

## 🚀 使用方法

### 基础命令

#### 1. 列出所有启动项
```python
# 列出所有启动项
list_startup_items()

# 只列出已启用的启动项
list_startup_items(filter_enabled=True)
```

#### 2. 启用/禁用启动项
```python
# 禁用指定启动项
disable_startup_item("Spotify")

# 启用指定启动项
enable_startup_item("Skype")
```

### 自然语言控制

#### 3. 智能语言控制
```python
# 禁用游戏相关启动项
natural_language_control("禁用所有游戏相关的启动项")

# 关闭Adobe软件自启动
natural_language_control("关闭Adobe相关的启动项")

# 只保留系统必需启动项
natural_language_control("禁用不必要的启动项，只保留系统必需的")

# 确认执行操作
natural_language_control("禁用所有游戏启动项", confirm=True)
```

### 性能分析和管理

#### 4. 性能分析
```python
# 获取启动性能分析报告
analyze_startup_performance()
```

#### 5. 备份和恢复
```python
# 备份当前启动项状态
backup_startup_state()

# 从备份恢复
restore_startup_state("/path/to/backup.json")
```

## 🌟 使用示例

### 场景1: 游戏玩家优化启动
```python
# 分析当前启动性能
analyze_startup_performance()

# 禁用游戏启动项（工作时）
natural_language_control("禁用Steam、Epic、Origin等游戏平台启动项", confirm=True)
```

### 场景2: 办公环境优化
```python
# 禁用娱乐软件，保留办公软件
natural_language_control("禁用音乐软件和游戏，保留Office和安全软件")

# 查看优化效果
analyze_startup_performance()
```

### 场景3: 系统清理
```python
# 先备份当前状态
backup_startup_state()

# 禁用所有可优化的启动项
natural_language_control("禁用所有可优化的启动项", confirm=True)

# 如果有问题，可以恢复
# restore_startup_state("备份文件路径")
```

## 🔧 支持的平台特性

### Windows
- **注册表启动项**: `HKCU\Run`, `HKLM\Run`
- **启动文件夹**: 用户和公共启动文件夹
- **任务计划程序**: 开机启动任务

### macOS  
- **LaunchAgents**: 用户和系统级启动代理
- **LaunchDaemons**: 系统守护进程
- **登录项**: 系统偏好设置中的启动项

### Linux
- **systemd服务**: 系统服务管理
- **自启动应用**: XDG autostart 标准
- **初始化脚本**: SysV init 兼容

## 🛡️ 安全特性

### 智能保护
- 自动识别关键系统启动项（安全软件、音频驱动等）
- 禁用关键启动项时显示警告
- 操作前自动创建备份

### 关键启动项保护列表
- 安全软件（防病毒、防火墙）
- 系统服务（音频、网络、蓝牙）
- 硬件驱动（显卡、输入设备）

## 📈 性能影响分析

### 影响级别说明
- **Critical**: 关键启动项，不建议禁用
- **High**: 对启动时间影响较大，建议根据需要禁用
- **Medium**: 中等影响，可根据个人需要选择

### 常见可优化启动项
- Adobe 系列软件更新程序
- 游戏平台（Steam、Epic Games）
- 云同步软件（Dropbox、OneDrive）
- 社交软件（QQ、微信、Skype）
- 音乐软件（Spotify、iTunes）

## 🔍 自然语言命令示例

### 中文命令
```
"禁用所有游戏相关的启动项"
"关闭Adobe软件的自启动"  
"只保留安全软件和系统必需的启动项"
"禁用不必要的更新程序"
"关闭所有聊天软件的开机启动"
"禁用云同步相关的启动项"
```

### 英文命令
```
"disable all game launchers"
"turn off adobe startup programs"
"remove unnecessary startup items"  
"disable music software autostart"
"keep only security and system apps"
```

## 🚨 注意事项

### 使用建议
1. **首次使用前务必备份**: 使用 `backup_startup_state()` 创建备份
2. **谨慎操作系统启动项**: 工具会自动保护，但请了解每个启动项的作用
3. **测试后再确认**: 先不加 `confirm=True` 参数查看匹配结果
4. **定期清理**: 建议每月检查一次启动项状态

### 权限要求
- **Windows**: 可能需要管理员权限修改某些注册表项
- **macOS**: 某些操作需要管理员密码确认
- **Linux**: systemd 操作可能需要 sudo 权限

## 🐛 故障排除

### 常见问题

**Q: 无法禁用某个启动项**
A: 检查是否有足够的系统权限，某些系统保护的启动项无法修改

**Q: 禁用后程序无法正常工作**  
A: 使用 `restore_startup_state()` 恢复备份，或手动重新启用相关启动项

**Q: 自然语言匹配不准确**
A: 尝试使用更具体的描述，或直接使用程序名称

## 📚 API参考

### 工具函数

#### `list_startup_items(filter_enabled=False)`
列出系统中的所有启动项
- `filter_enabled`: 是否只显示已启用的启动项

#### `disable_startup_item(item_name)`  
禁用指定名称的启动项
- `item_name`: 启动项名称（不区分大小写）

#### `enable_startup_item(item_name)`
启用指定名称的启动项
- `item_name`: 启动项名称（不区分大小写）

#### `natural_language_control(command, confirm=False)`
使用自然语言控制启动项
- `command`: 自然语言命令
- `confirm`: 是否确认执行操作

#### `analyze_startup_performance()`
分析启动性能并提供优化建议

#### `backup_startup_state()`
备份当前启动项状态到文件

#### `restore_startup_state(backup_file)`
从备份文件恢复启动项状态
- `backup_file`: 备份文件路径

## 📄 许可证

本项目采用 MIT 许可证。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！

---

**⚠️ 重要提醒**: 修改系统启动项可能影响系统稳定性，请谨慎操作并在操作前备份系统状态。