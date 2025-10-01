import json
import random
import string
from typing import Dict

from dotenv import find_dotenv, load_dotenv
from pydantic import Field, computed_field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

SYSTEM_VERSION = "0.1.0"


def generate_hostid(length: int = 20) -> str:
    """生成 host-id

    Returns:
        str: host-id
    """
    return "py-" + "".join(random.choice(string.digits) for _ in range(length - 3))


class SnailJobSettings(BaseSettings):
    """Snail Job 配置类，基于 Pydantic Settings"""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # 服务器配置
    snail_use_grpc: bool = Field(default=True, description="是否使用 gRPC 协议")
    snail_server_host: str = Field(default="127.0.0.1", description="服务器主机地址")
    snail_server_port: str = Field(default="17888", description="服务器端口")

    # 客户端配置
    snail_version: str = Field(default="1.1.0", description="客户端版本")
    snail_host_ip: str = Field(default="127.0.0.1", description="客户端主机IP")
    snail_host_port: str = Field(default="17889", description="客户端端口")
    snail_namespace: str = Field(default="764d604ec6fc45f68cd92514c40e9e1a", description="命名空间")
    snail_group_name: str = Field(default="snail_job_demo_group", description="组名")
    snail_token: str = Field(default="SJ_Wyz3dmsdbDOkDujOTSSoBjGQP1BMsVnj", description="认证令牌")
    snail_labels: str = Field(default="env:dev,app:demo", description="标签配置")

    # 日志配置
    snail_log_level: str = Field(default="INFO", description="日志级别")
    snail_log_format: str = Field(
        default="%(asctime)s | %(name)-22s | %(levelname)-8s | %(message)s", description="日志格式"
    )
    snail_log_remote_interval: int = Field(default=10, description="远程日志上报间隔(秒)")
    snail_log_remote_buffer_size: int = Field(default=10, description="远程日志缓冲区大小")
    snail_log_local_filename: str = Field(default="log/snailjob.log", description="本地日志文件名")
    snail_log_local_backup_count: int = Field(default=2, description="本地日志备份数量")

    # 系统配置
    executor_type_python: str = Field(default="2", description="Python执行器类型")
    system_version: str = Field(default=SYSTEM_VERSION, description="系统版本", const=True)
    root_map: str = Field(default="ROOT_MAP", description="根映射")

    @field_validator("snail_use_grpc", mode="before")
    @classmethod
    def validate_grpc(cls, v):
        """验证 gRPC 配置"""
        if isinstance(v, str):
            return v.lower() == "true"
        return bool(v)

    @field_validator("snail_log_level")
    @classmethod
    def validate_log_level(cls, v):
        """验证日志级别"""
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if v.upper() not in valid_levels:
            raise ValueError(f"日志级别必须是以下之一: {valid_levels}")
        return v.upper()

    @computed_field
    @property
    def snail_host_id(self) -> str:
        """生成的主机ID"""
        return generate_hostid()

    @computed_field
    @property
    def label_dict(self) -> Dict[str, str]:
        """解析标签字典"""
        labels = {}
        for item in self.snail_labels.split(","):
            if ":" in item:
                key, value = item.split(":", 1)
                labels[key.strip()] = value.strip()
        labels["state"] = "up"
        return labels

    @computed_field
    @property
    def snail_headers(self) -> Dict[str, str]:
        """生成请求头"""
        return {
            "host-id": self.snail_host_id,
            "host-ip": self.snail_host_ip,
            "version": self.snail_version,
            "host-port": self.snail_host_port,
            "namespace": self.snail_namespace,
            "group-name": self.snail_group_name,
            "token": self.snail_token,
            "content-type": "application/json",
            "executor-type": self.executor_type_python,
            "system-version": self.system_version,
            "label": json.dumps(self.label_dict),
        }


# 全局配置实例 - 延迟初始化
_settings: SnailJobSettings | None = None


def get_snailjob_settings() -> SnailJobSettings:
    """获取配置实例，支持延迟初始化

    Returns:
        SnailJobSettings: 配置实例
    """
    global _settings
    if _settings is None:
        _ = load_dotenv(find_dotenv())
        _settings = SnailJobSettings()
    return _settings


def configure_settings(**kwargs) -> SnailJobSettings:
    """配置设置，允许用户自定义配置

    Args:
        **kwargs: 配置参数

    Returns:
        SnailJobSettings: 新的配置实例

    Example:
        >>> from snailjob.settings import configure_settings
        >>> settings = configure_settings(snail_server_host="192.168.1.100")
    """
    global _settings
    _settings = SnailJobSettings(**kwargs)
    return _settings
