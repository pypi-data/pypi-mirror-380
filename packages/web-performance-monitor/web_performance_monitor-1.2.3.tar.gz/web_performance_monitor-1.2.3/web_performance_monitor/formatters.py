"""
格式化工具模块

提供各种数据格式化功能
"""

import json
from typing import Dict, Any

from .models import PerformanceMetrics


class NotificationFormatter:
    """
    通知格式化器
    负责格式化告警消息和文件名
    """

    @staticmethod
    def format_alert_message(metrics: PerformanceMetrics) -> str:
        """格式化告警消息，包含请求URL、参数、响应时间等信息

        Args:
            metrics: 性能指标数据

        Returns:
            str: 格式化的告警消息
        """
        # 格式化请求参数
        params_str = json.dumps(metrics.request_params, ensure_ascii=False, indent=2)
        if len(params_str) > 500:  # 限制参数长度
            params_str = params_str[:500] + "...(截断)"

        return f"""🚨 性能告警报告

📍 接口信息:
   端点: {metrics.endpoint}
   URL: {metrics.request_url}
   方法: {metrics.request_method}
   状态码: {metrics.status_code}

⏱️ 性能数据:
   响应时间: {metrics.execution_time:.2f}秒
   告警时间: {metrics.timestamp.strftime('%Y-%m-%d %H:%M:%S')}

📋 请求参数:
{params_str}

---
此告警由Web性能监控工具自动生成
"""

    @staticmethod
    def format_mattermost_message(metrics: PerformanceMetrics) -> str:
        """格式化Mattermost消息

        Args:
            metrics: 性能指标数据

        Returns:
            str: 格式化的Mattermost消息
        """
        # 表头
        table = "| 时间 | 接口 | URL | 方法 | 响应时间 | 状态码 |\n"
        table += "|------|------|------|------|----------|--------|\n"
        table += f"| {metrics.timestamp.strftime('%Y-%m-%d %H:%M:%S')} | " \
                 f"{metrics.endpoint} | {metrics.request_url} | " \
                 f"{metrics.request_method} | **{metrics.execution_time:.2f}秒** | " \
                 f"{metrics.status_code} |\n"
        return f"""####  🚨 性能告警 \n {table}"""

    @staticmethod
    def generate_filename(metrics: PerformanceMetrics, extension: str = "html") -> str:
        """生成包含时间戳和接口信息的唯一文件名

        Args:
            metrics: 性能指标数据
            extension: 文件扩展名

        Returns:
            str: 生成的文件名
        """
        # 清理端点名称，移除特殊字符
        safe_endpoint = (metrics.endpoint
                         .replace('/', '_')
                         .replace('<', '')
                         .replace('>', '')
                         .replace(':', '')
                         .replace('?', '')
                         .replace('&', '_')
                         .replace('=', '_')
                         .replace(' ', '_')
                         .replace('-', '_'))

        # 限制端点名称长度
        if len(safe_endpoint) > 50:
            safe_endpoint = safe_endpoint[:50]

        return f"peralert_{safe_endpoint}.{extension}"

    @staticmethod
    def format_log_message(metrics: PerformanceMetrics, file_path: str = None) -> str:
        """格式化日志消息

        Args:
            metrics: 性能指标数据
            file_path: 文件路径（可选）

        Returns:
            str: 格式化的日志消息
        """
        base_msg = (f"性能告警触发: {metrics.request_method} {metrics.endpoint} "
                    f"响应时间={metrics.execution_time:.2f}s")

        if file_path:
            base_msg += f" 报告已保存至: {file_path}"

        return base_msg


class ConfigFormatter:
    """配置格式化器"""

    @staticmethod
    def format_config_summary(config_dict: Dict[str, Any]) -> str:
        """格式化配置摘要

        Args:
            config_dict: 配置字典

        Returns:
            str: 格式化的配置摘要
        """
        summary = "📋 当前配置:\n"

        # 性能配置
        summary += f"  ⏱️  响应时间阈值: {config_dict.get('threshold_seconds', 'N/A')}秒\n"
        summary += f"  📅 告警窗口: {config_dict.get('alert_window_days', 'N/A')}天\n"
        summary += f"  📊 最大开销: {config_dict.get('max_performance_overhead', 'N/A') * 100:.1f}%\n"

        # 通知配置
        summary += f"  📁 本地文件: {'启用' if config_dict.get('enable_local_file') else '禁用'}\n"
        if config_dict.get('enable_local_file'):
            summary += f"     输出目录: {config_dict.get('local_output_dir', 'N/A')}\n"

        summary += f"  💬 Mattermost: {'启用' if config_dict.get('enable_mattermost') else '禁用'}\n"
        if config_dict.get('enable_mattermost'):
            summary += f"     服务器: {config_dict.get('mattermost_server_url', 'N/A')}\n"
            summary += f"     频道: {config_dict.get('mattermost_channel_id', 'N/A')}\n"

        return summary
