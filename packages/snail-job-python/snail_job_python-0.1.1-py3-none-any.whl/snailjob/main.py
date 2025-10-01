import asyncio
import threading
import time

from snailjob.exec import ExecutorManager
from snailjob.grpc import run_grpc_server
from snailjob.http import run_http_server
from snailjob.log import SnailLog
from snailjob.rpc import send_heartbeat
from snailjob.settings import get_snailjob_settings

# 全局配置实例
settings = get_snailjob_settings()


class HeartbeatTask:
    """心跳发送任务"""

    def __init__(self) -> None:
        self._thread = threading.Thread(target=self._send_heartbeats, daemon=True)
        self.event = threading.Event()

    def _send_heartbeats(self):
        while not self.event.is_set():
            send_heartbeat()
            time.sleep(28)

    def run(self):
        self._thread.start()


def client_main():
    """客户端主函数"""
    heartbeat_task = HeartbeatTask()
    heartbeat_task.run()
    ExecutorManager.register_executors_to_server()

    if settings.snail_use_grpc:
        run_grpc_server(settings.snail_host_port)
    else:
        try:
            asyncio.run(run_http_server(settings.snail_host_port))
        except KeyboardInterrupt:
            SnailLog.LOCAL.info("KeyboardInterrupt, 退出程序")
        except Exception as ex:
            heartbeat_task.event.set()
            SnailLog.LOCAL.error(f"程序发生异常，正在退出: {ex}")
