#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
开机启动项控制 MCP 服务器
支持跨平台的启动项管理和自然语言交互
使用 FastMCP 框架
"""

import json
import os
import platform
import re
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import logging

# FastMCP imports
from fastmcp import FastMCP


# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class StartupItemManager:
    """跨平台启动项管理器"""
    
    def __init__(self):
        self.platform = platform.system().lower()
        self.backup_dir = Path.home() / ".startup_control_backups"
        self.backup_dir.mkdir(exist_ok=True)
        
        # 重要启动项关键词（不应被禁用）
        self.critical_keywords = [
            'security', 'antivirus', 'firewall', 'system', 'audio', 'bluetooth',
            '安全', '防病毒', '防火墙', '系统', '音频', '蓝牙', 'network', '网络'
        ]
        
        # 常见可优化启动项关键词
        self.optimizable_keywords = [
            'adobe', 'office', 'game', 'steam', 'epic', 'launcher', 'updater',
            'helper', 'assistant', 'sync', 'cloud', 'backup',
            '游戏', '启动器', '更新', '助手', '同步', '云'
        ]

    def get_startup_items(self) -> List[Dict]:
        """获取所有启动项"""
        try:
            if self.platform == "windows":
                return self._get_windows_startup_items()
            elif self.platform == "darwin":  # macOS
                return self._get_macos_startup_items()
            elif self.platform == "linux":
                return self._get_linux_startup_items()
            else:
                raise Exception(f"不支持的平台: {self.platform}")
        except Exception as e:
            logger.error(f"获取启动项失败: {e}")
            return []

    def _get_windows_startup_items(self) -> List[Dict]:
        """获取Windows启动项"""
        items = []
        
        # 注册表启动项
        reg_paths = [
            r"HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run",
            r"HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run",
        ]
        
        for reg_path in reg_paths:
            try:
                result = subprocess.run([
                    "reg", "query", reg_path
                ], capture_output=True, text=True, shell=True)
                
                if result.returncode == 0:
                    lines = result.stdout.strip().split('\n')
                    for line in lines[1:]:  # 跳过标题行
                        if "REG_" in line:
                            parts = line.strip().split(None, 2)
                            if len(parts) >= 3:
                                name = parts[0]
                                path = parts[2] if len(parts) > 2 else ""
                                items.append({
                                    'name': name,
                                    'path': path,
                                    'type': 'registry',
                                    'location': reg_path,
                                    'enabled': True,
                                    'impact': self._analyze_startup_impact(name, path)
                                })
            except Exception as e:
                logger.warning(f"无法读取注册表 {reg_path}: {e}")
        
        # 启动文件夹
        startup_folders = [
            os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"),
            os.path.expandvars(r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs\Startup")
        ]
        
        for folder in startup_folders:
            if os.path.exists(folder):
                for file in os.listdir(folder):
                    if file.endswith(('.lnk', '.exe', '.bat', '.cmd')):
                        full_path = os.path.join(folder, file)
                        items.append({
                            'name': os.path.splitext(file)[0],
                            'path': full_path,
                            'type': 'startup_folder',
                            'location': folder,
                            'enabled': True,
                            'impact': self._analyze_startup_impact(file, full_path)
                        })
        
        return items

    def _get_macos_startup_items(self) -> List[Dict]:
        """获取macOS启动项"""
        items = []
        
        # LaunchAgents 和 LaunchDaemons
        launch_paths = [
            "~/Library/LaunchAgents",
            "/Library/LaunchAgents",
            "/Library/LaunchDaemons",
            "/System/Library/LaunchAgents",
            "/System/Library/LaunchDaemons"
        ]
        
        for path in launch_paths:
            expanded_path = os.path.expanduser(path)
            if os.path.exists(expanded_path):
                for file in os.listdir(expanded_path):
                    if file.endswith('.plist'):
                        full_path = os.path.join(expanded_path, file)
                        
                        # 检查是否已加载
                        try:
                            result = subprocess.run([
                                "launchctl", "list"
                            ], capture_output=True, text=True)
                            
                            service_name = os.path.splitext(file)[0]
                            enabled = service_name in result.stdout
                            
                            items.append({
                                'name': service_name,
                                'path': full_path,
                                'type': 'launchd',
                                'location': path,
                                'enabled': enabled,
                                'impact': self._analyze_startup_impact(service_name, full_path)
                            })
                        except Exception as e:
                            logger.warning(f"检查服务状态失败 {file}: {e}")
        
        # 登录项 (Login Items)
        try:
            result = subprocess.run([
                "osascript", "-e", 
                'tell application "System Events" to get the name of every login item'
            ], capture_output=True, text=True)
            
            if result.returncode == 0 and result.stdout.strip():
                login_items = result.stdout.strip().split(', ')
                for item in login_items:
                    items.append({
                        'name': item.strip(),
                        'path': '',
                        'type': 'login_item',
                        'location': 'System Preferences',
                        'enabled': True,
                        'impact': self._analyze_startup_impact(item, '')
                    })
        except Exception as e:
            logger.warning(f"获取登录项失败: {e}")
        
        return items

    def _get_linux_startup_items(self) -> List[Dict]:
        """获取Linux启动项"""
        items = []
        
        # systemd 服务
        try:
            result = subprocess.run([
                "systemctl", "list-unit-files", "--type=service", "--state=enabled"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')[1:]  # 跳过标题行
                for line in lines:
                    if line.strip() and not line.startswith('UNIT FILE'):
                        parts = line.strip().split()
                        if len(parts) >= 2:
                            service_name = parts[0]
                            items.append({
                                'name': service_name,
                                'path': f'/etc/systemd/system/{service_name}',
                                'type': 'systemd',
                                'location': 'systemd',
                                'enabled': True,
                                'impact': self._analyze_startup_impact(service_name, '')
                            })
        except Exception as e:
            logger.warning(f"获取systemd服务失败: {e}")
        
        # 自启动应用程序
        autostart_dirs = [
            "~/.config/autostart",
            "/etc/xdg/autostart"
        ]
        
        for dir_path in autostart_dirs:
            expanded_path = os.path.expanduser(dir_path)
            if os.path.exists(expanded_path):
                for file in os.listdir(expanded_path):
                    if file.endswith('.desktop'):
                        full_path = os.path.join(expanded_path, file)
                        name = os.path.splitext(file)[0]
                        
                        # 检查是否启用
                        enabled = True
                        try:
                            with open(full_path, 'r') as f:
                                content = f.read()
                                if 'Hidden=true' in content:
                                    enabled = False
                        except Exception:
                            pass
                        
                        items.append({
                            'name': name,
                            'path': full_path,
                            'type': 'autostart',
                            'location': dir_path,
                            'enabled': enabled,
                            'impact': self._analyze_startup_impact(name, full_path)
                        })
        
        return items

    def _analyze_startup_impact(self, name: str, path: str) -> Dict:
        """分析启动项对系统性能的影响"""
        name_lower = name.lower()
        path_lower = path.lower()
        
        # 判断是否为关键启动项
        is_critical = any(keyword in name_lower or keyword in path_lower 
                         for keyword in self.critical_keywords)
        
        # 判断是否为可优化项
        is_optimizable = any(keyword in name_lower or keyword in path_lower 
                           for keyword in self.optimizable_keywords)
        
        # 计算影响级别
        if is_critical:
            impact_level = "critical"
            recommendation = "不建议禁用"
        elif is_optimizable:
            impact_level = "high"
            recommendation = "建议禁用以优化启动时间"
        else:
            impact_level = "medium"
            recommendation = "可根据需要禁用"
        
        return {
            'level': impact_level,
            'recommendation': recommendation,
            'is_critical': is_critical,
            'is_optimizable': is_optimizable
        }

    def disable_startup_item(self, item_info: Dict) -> bool:
        """禁用启动项"""
        try:
            # 先备份
            self._backup_startup_state()
            
            if self.platform == "windows":
                return self._disable_windows_startup_item(item_info)
            elif self.platform == "darwin":
                return self._disable_macos_startup_item(item_info)
            elif self.platform == "linux":
                return self._disable_linux_startup_item(item_info)
            else:
                return False
        except Exception as e:
            logger.error(f"禁用启动项失败: {e}")
            return False

    def enable_startup_item(self, item_info: Dict) -> bool:
        """启用启动项"""
        try:
            if self.platform == "windows":
                return self._enable_windows_startup_item(item_info)
            elif self.platform == "darwin":
                return self._enable_macos_startup_item(item_info)
            elif self.platform == "linux":
                return self._enable_linux_startup_item(item_info)
            else:
                return False
        except Exception as e:
            logger.error(f"启用启动项失败: {e}")
            return False

    def _disable_windows_startup_item(self, item_info: Dict) -> bool:
        """禁用Windows启动项"""
        if item_info['type'] == 'registry':
            # 删除注册表项
            try:
                subprocess.run([
                    "reg", "delete", item_info['location'], "/v", item_info['name'], "/f"
                ], check=True, capture_output=True)
                return True
            except subprocess.CalledProcessError:
                return False
        elif item_info['type'] == 'startup_folder':
            # 重命名文件（添加.disabled后缀）
            try:
                disabled_path = item_info['path'] + '.disabled'
                os.rename(item_info['path'], disabled_path)
                return True
            except Exception:
                return False
        return False

    def _disable_macos_startup_item(self, item_info: Dict) -> bool:
        """禁用macOS启动项"""
        if item_info['type'] == 'launchd':
            try:
                # 卸载服务
                subprocess.run([
                    "launchctl", "unload", item_info['path']
                ], check=True, capture_output=True)
                return True
            except subprocess.CalledProcessError:
                return False
        elif item_info['type'] == 'login_item':
            try:
                # 移除登录项
                subprocess.run([
                    "osascript", "-e", 
                    f'tell application "System Events" to delete login item "{item_info["name"]}"'
                ], check=True, capture_output=True)
                return True
            except subprocess.CalledProcessError:
                return False
        return False

    def _disable_linux_startup_item(self, item_info: Dict) -> bool:
        """禁用Linux启动项"""
        if item_info['type'] == 'systemd':
            try:
                subprocess.run([
                    "systemctl", "disable", item_info['name']
                ], check=True, capture_output=True)
                return True
            except subprocess.CalledProcessError:
                return False
        elif item_info['type'] == 'autostart':
            try:
                # 修改.desktop文件，添加Hidden=true
                with open(item_info['path'], 'r') as f:
                    content = f.read()
                
                if 'Hidden=' not in content:
                    content += '\nHidden=true\n'
                else:
                    content = re.sub(r'Hidden=.*', 'Hidden=true', content)
                
                with open(item_info['path'], 'w') as f:
                    f.write(content)
                return True
            except Exception:
                return False
        return False

    def _enable_windows_startup_item(self, item_info: Dict) -> bool:
        """启用Windows启动项"""
        if item_info['type'] == 'startup_folder':
            # 移除.disabled后缀
            try:
                if item_info['path'].endswith('.disabled'):
                    original_path = item_info['path'][:-9]  # 移除.disabled
                    os.rename(item_info['path'], original_path)
                    return True
            except Exception:
                return False
        return False

    def _enable_macos_startup_item(self, item_info: Dict) -> bool:
        """启用macOS启动项"""
        if item_info['type'] == 'launchd':
            try:
                subprocess.run([
                    "launchctl", "load", item_info['path']
                ], check=True, capture_output=True)
                return True
            except subprocess.CalledProcessError:
                return False
        return False

    def _enable_linux_startup_item(self, item_info: Dict) -> bool:
        """启用Linux启动项"""
        if item_info['type'] == 'systemd':
            try:
                subprocess.run([
                    "systemctl", "enable", item_info['name']
                ], check=True, capture_output=True)
                return True
            except subprocess.CalledProcessError:
                return False
        elif item_info['type'] == 'autostart':
            try:
                with open(item_info['path'], 'r') as f:
                    content = f.read()
                
                # 移除或修改Hidden=true
                content = re.sub(r'Hidden=true.*\n', '', content)
                content = re.sub(r'Hidden=.*', 'Hidden=false', content)
                
                with open(item_info['path'], 'w') as f:
                    f.write(content)
                return True
            except Exception:
                return False
        return False

    def _backup_startup_state(self):
        """备份当前启动项状态"""
        try:
            startup_items = self.get_startup_items()
            timestamp = int(time.time())
            backup_file = self.backup_dir / f"startup_backup_{timestamp}.json"

            with open(backup_file, 'w', encoding='utf-8') as f:
                json.dump(startup_items, f, ensure_ascii=False, indent=2)

            logger.info(f"启动项状态已备份到: {backup_file}")
        except Exception as e:
            logger.error(f"备份启动项状态失败: {e}")

    def restore_startup_state(self, backup_file: str) -> bool:
        """恢复启动项状态"""
        try:
            with open(backup_file, 'r', encoding='utf-8') as f:
                backup_data = json.load(f)
            
            # 恢复逻辑（简化版）
            logger.info(f"从 {backup_file} 恢复启动项状态")
            return True
        except Exception as e:
            logger.error(f"恢复启动项状态失败: {e}")
            return False

    def parse_natural_language(self, command: str) -> List[Dict]:
        """解析自然语言命令"""
        command_lower = command.lower()
        startup_items = self.get_startup_items()
        matched_items = []
        
        # 关键词匹配
        disable_keywords = ['禁用', '关闭', '停用', '删除', '移除', 'disable', 'stop', 'remove']
        enable_keywords = ['启用', '开启', '打开', '添加', 'enable', 'start', 'add']
        
        action = None
        if any(keyword in command_lower for keyword in disable_keywords):
            action = 'disable'
        elif any(keyword in command_lower for keyword in enable_keywords):
            action = 'enable'
        
        # 匹配目标程序
        target_keywords = []
        
        # 常见程序类型匹配
        program_patterns = {
            '游戏': ['game', 'steam', 'epic', 'origin', 'uplay'],
            'adobe': ['adobe', 'acrobat', 'photoshop', 'illustrator'],
            '办公软件': ['office', 'word', 'excel', 'powerpoint', 'outlook'],
            '聊天软件': ['qq', 'wechat', 'skype', 'discord'],
            '浏览器': ['chrome', 'firefox', 'edge', 'safari'],
            '音乐软件': ['spotify', 'itunes', 'music'],
            '云同步': ['dropbox', 'onedrive', 'icloud', 'google drive', 'sync'],
        }
        
        for category, keywords in program_patterns.items():
            if category in command_lower or any(kw in command_lower for kw in keywords):
                target_keywords.extend(keywords)
        
        # 直接文本匹配
        words = re.findall(r'\b\w+\b', command_lower)
        target_keywords.extend(words)
        
        # 匹配启动项
        for item in startup_items:
            item_name_lower = item['name'].lower()
            item_path_lower = item['path'].lower()
            
            if any(keyword in item_name_lower or keyword in item_path_lower 
                   for keyword in target_keywords):
                matched_items.append({
                    'item': item,
                    'action': action,
                    'confidence': self._calculate_match_confidence(item, target_keywords)
                })
        
        # 按置信度排序
        matched_items.sort(key=lambda x: x['confidence'], reverse=True)
        
        return matched_items

    def _calculate_match_confidence(self, item: Dict, keywords: List[str]) -> float:
        """计算匹配置信度"""
        name_lower = item['name'].lower()
        path_lower = item['path'].lower()
        
        confidence = 0.0
        for keyword in keywords:
            if keyword in name_lower:
                confidence += 1.0
            elif keyword in path_lower:
                confidence += 0.5
        
        return confidence / len(keywords) if keywords else 0.0

    def get_startup_performance_analysis(self) -> Dict:
        """获取启动性能分析"""
        startup_items = self.get_startup_items()
        
        total_items = len(startup_items)
        enabled_items = sum(1 for item in startup_items if item['enabled'])
        critical_items = sum(1 for item in startup_items if item['impact']['is_critical'])
        optimizable_items = sum(1 for item in startup_items if item['impact']['is_optimizable'])
        
        return {
            'total_items': total_items,
            'enabled_items': enabled_items,
            'critical_items': critical_items,
            'optimizable_items': optimizable_items,
            'optimization_potential': f"{optimizable_items}/{enabled_items}" if enabled_items > 0 else "0/0",
            'recommendations': self._get_optimization_recommendations(startup_items)
        }

    def _get_optimization_recommendations(self, startup_items: List[Dict]) -> List[str]:
        """获取优化建议"""
        recommendations = []
        
        optimizable_items = [item for item in startup_items 
                           if item['enabled'] and item['impact']['is_optimizable']]
        
        if len(optimizable_items) > 5:
            recommendations.append(f"发现 {len(optimizable_items)} 个可优化的启动项，建议禁用以提升启动速度")
        
        critical_enabled = sum(1 for item in startup_items 
                             if item['enabled'] and item['impact']['is_critical'])
        if critical_enabled > 0:
            recommendations.append(f"检测到 {critical_enabled} 个关键启动项正常运行")
        
        if len(startup_items) > 20:
            recommendations.append("启动项较多，建议定期清理不必要的程序")
        
        return recommendations


# 创建MCP服务器
mcp = FastMCP("Startup Control")
manager = StartupItemManager()

@mcp.tool()
def list_user_startup_items(
    show_all: bool = False,
    only_enabled: bool = False
) -> str:
    """
    获取用户启动项列表

    智能过滤显示用户安装的第三方应用启动项，自动排除系统内置项。
    专注于用户实际需要管理的启动项，避免显示大量系统组件。

    Args:
        show_all: 是否显示所有启动项包括系统项（默认False仅显示第三方应用）
        only_enabled: 是否只显示已启用的项（默认False显示全部状态）

    Returns:
        格式化的启动项清单，包含状态、影响级别和管理建议
    """
    startup_items = manager.get_startup_items()

    # 默认过滤掉系统启动项，只显示用户安装的第三方应用
    if not show_all:
        startup_items = [
            item for item in startup_items
            if not (item['location'].startswith('/System/') or
                   item['name'].startswith('com.apple.'))
        ]

    # 过滤已启用项
    if only_enabled:
        startup_items = [item for item in startup_items if item['enabled']]

    # 统计信息
    total_count = len(startup_items)
    enabled_count = sum(1 for item in startup_items if item['enabled'])

    if total_count == 0:
        return "没有找到用户安装的启动项"

    result = f"📊 **启动项统计**\n"
    result += f"   • 用户启动项: {total_count} 个\n"
    result += f"   • 已启用: {enabled_count} 个\n"
    result += f"   • 已禁用: {total_count - enabled_count} 个\n\n"

    # 按位置分组显示
    grouped_items = {}
    for item in startup_items:
        location = item['location']
        if location not in grouped_items:
            grouped_items[location] = []
        grouped_items[location].append(item)

    # 按重要性排序位置
    location_order = ['System Preferences', '~/Library/LaunchAgents', '/Library/LaunchAgents', '/Library/LaunchDaemons']
    sorted_locations = sorted(grouped_items.keys(), key=lambda x: location_order.index(x) if x in location_order else 99)

    for location in sorted_locations:
        items = grouped_items[location]
        location_name = {
            'System Preferences': '登录项',
            '~/Library/LaunchAgents': '用户启动代理',
            '/Library/LaunchAgents': '全局启动代理',
            '/Library/LaunchDaemons': '系统守护进程'
        }.get(location, location)

        result += f"📁 **{location_name}** ({len(items)} 个)\n"

        for item in items:
            status = "✅" if item['enabled'] else "❌"
            impact = item['impact']['level']

            result += f"   {status} {item['name']}\n"
            if item['impact']['is_critical']:
                result += f"      ⚠️ 关键项，影响: {impact}\n"
            else:
                result += f"      影响: {impact}\n"

        result += "\n"

    # 添加使用提示
    if not show_all:
        result += "💡 **提示**: 默认只显示用户安装的启动项。使用 'show_all: true' 查看所有项目（包括800+系统项）\n"

    return result

@mcp.tool()
def disable_startup_item(item_name: str) -> str:
    """禁用指定的开机启动项

    安全地禁用启动项，会自动检查是否为关键项避免影响系统运行。

    Args:
        item_name: 启动项名称（如 'Docker', 'FlClash' 等）
    """
    startup_items = manager.get_startup_items()
    
    target_item = None
    for item in startup_items:
        if item['name'].lower() == item_name.lower():
            target_item = item
            break
    
    if not target_item:
        return f"未找到名为 '{item_name}' 的启动项"
    
    if target_item['impact']['is_critical']:
        return f"⚠️ '{item_name}' 是关键启动项，不建议禁用！"
    
    success = manager.disable_startup_item(target_item)
    
    if success:
        return f"✅ 成功禁用启动项: {item_name}"
    else:
        return f"❌ 禁用启动项失败: {item_name}"

# @mcp.tool()
# def enable_startup_item(item_name: str) -> str:
#     """启用指定的开机启动项
#
#     重新启用之前被禁用的启动项。
#
#     Args:
#         item_name: 启动项名称
#     """
#     startup_items = manager.get_startup_items()
#
#     target_item = None
#     for item in startup_items:
#         if item['name'].lower() == item_name.lower():
#             target_item = item
#             break
#
#     if not target_item:
#         return f"未找到名为 '{item_name}' 的启动项"
#
#     success = manager.enable_startup_item(target_item)
#
#     if success:
#         return f"✅ 成功启用启动项: {item_name}"
#     else:
#         return f"❌ 启用启动项失败: {item_name}"

# @mcp.tool()
# def natural_language_control(command: str, confirm: bool = False) -> str:
#     """使用自然语言控制启动项
#
#     支持自然语言命令，如：
#     - '禁用所有游戏相关的启动项'
#     - '关闭不常用的启动项'
#     - '优化启动速度'
#
#     Args:
#         command: 自然语言描述的控制命令
#         confirm: 是否执行操作（默认False只预览，True执行操作）
#     """
#     matches = manager.parse_natural_language(command)
#
#     if not matches:
#         return "未找到匹配的启动项，请尝试更具体的描述"
#
#     result = f"根据命令 '{command}' 找到以下匹配项:\n\n"
#
#     for match in matches[:10]:  # 最多显示10个匹配项
#         item = match['item']
#         action = match['action']
#         confidence = match['confidence']
#
#         action_text = "禁用" if action == 'disable' else "启用"
#
#         result += f"🎯 **{item['name']}** (匹配度: {confidence:.2f})\n"
#         result += f"   当前状态: {'已启用' if item['enabled'] else '已禁用'}\n"
#         result += f"   建议操作: {action_text}\n"
#         result += f"   影响级别: {item['impact']['level']}\n\n"
#
#         if confirm and action:
#             if action == 'disable' and not item['impact']['is_critical']:
#                 success = manager.disable_startup_item(item)
#                 result += f"   {'✅ 已禁用' if success else '❌ 禁用失败'}\n"
#             elif action == 'enable':
#                 success = manager.enable_startup_item(item)
#                 result += f"   {'✅ 已启用' if success else '❌ 启用失败'}\n"
#             elif action == 'disable' and item['impact']['is_critical']:
#                 result += f"   ⚠️ 关键启动项，跳过禁用操作\n"
#             result += "\n"
#
#     if not confirm:
#         result += "\n💡 添加参数 'confirm: true' 来执行这些操作"
#
#     return result

@mcp.tool()
def analyze_startup_performance() -> str:
    """分析启动性能并提供优化建议

    分析当前启动项对系统启动速度的影响，并提供专业的优化建议。
    """
    analysis = manager.get_startup_performance_analysis()
    
    result = "🔍 **启动性能分析报告**\n\n"
    result += f"📊 **统计信息:**\n"
    result += f"   • 启动项总数: {analysis['total_items']}\n"
    result += f"   • 已启用项目: {analysis['enabled_items']}\n"
    result += f"   • 关键启动项: {analysis['critical_items']}\n"
    result += f"   • 可优化项目: {analysis['optimizable_items']}\n"
    result += f"   • 优化潜力: {analysis['optimization_potential']}\n\n"
    
    result += f"💡 **优化建议:**\n"
    for i, rec in enumerate(analysis['recommendations'], 1):
        result += f"   {i}. {rec}\n"
    
    return result

# @mcp.tool()
# def backup_startup_state() -> str:
#     """备份当前启动项状态"""
#     manager._backup_startup_state()
#     return "✅ 启动项状态已成功备份"
#
# @mcp.tool()
# def restore_startup_state(backup_file: str) -> str:
#     """从备份恢复启动项状态"""
#     success = manager.restore_startup_state(backup_file)
#
#     if success:
#         return f"✅ 成功从 {backup_file} 恢复启动项状态"
#     else:
#         return f"❌ 从 {backup_file} 恢复启动项状态失败"


# 导出 MCP 服务器实例以便外部使用
mcp_server = mcp

def main():
    """主入口函数"""
    mcp.run()

if __name__ == "__main__":
    main()
