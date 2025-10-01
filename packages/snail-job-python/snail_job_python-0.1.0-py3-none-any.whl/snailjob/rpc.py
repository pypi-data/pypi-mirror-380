from typing import List

from snailjob.schemas import (
    DispatchJobResult,
    JobExecutor,
    JobLogTask,
    MapTaskRequest,
    SnailJobRequest,
    StatusEnum,
)
from snailjob.settings import get_snailjob_settings

# 全局配置实例
settings = get_snailjob_settings()


def _get_send_function():
    """根据配置获取发送函数"""
    if settings.snail_use_grpc:
        from snailjob.grpc import send_to_server
    else:
        from snailjob.http import send_to_server
    return send_to_server


def send_heartbeat():
    """注册客户端(心跳)"""
    URI = "/beat"
    payload = SnailJobRequest.build(["PING"])
    send_to_server = _get_send_function()
    return send_to_server(URI, payload.model_dump(), "发送心跳")


def send_dispatch_result(payload: DispatchJobResult) -> StatusEnum:
    """执行结果上报"""
    URI = "/report/dispatch/result"
    send_to_server = _get_send_function()
    return send_to_server(URI, payload.model_dump(), "结果上报")


def send_batch_log_report(payload: List[JobLogTask]) -> StatusEnum:
    """日志批量上报"""
    URI = "/batch/server/report/log"
    send_to_server = _get_send_function()
    return send_to_server(URI, [log.model_dump() for log in payload], "日志批量上报")


def send_batch_map_report(payload: MapTaskRequest) -> StatusEnum:
    """生成同步MAP任务"""
    URI = "/batch/report/job/map/task/v1"
    send_to_server = _get_send_function()
    return send_to_server(URI, payload.model_dump(), "生成同步MAP任务")


def register_executors(payload: List[JobExecutor]) -> StatusEnum:
    """注册执行器"""
    URI = "/register/job/executors"
    send_to_server = _get_send_function()
    return send_to_server(URI, [item.model_dump() for item in payload], "注册执行器")
