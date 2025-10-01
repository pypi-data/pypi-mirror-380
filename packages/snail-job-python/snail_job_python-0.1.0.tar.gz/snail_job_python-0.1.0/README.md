<p align="center">
  <a href="https://snailjob.opensnail.com">
   <img alt="snail-job-Logo" src="doc/images/favicon.svg" width="200px">
  </a>
</p>

<p align="center">
    🔥🔥🔥 灵活，可靠和快速的分布式任务重试和分布式任务调度平台 <br/>
</p>

<p align="center">

> ✅️ 可重放，可管控、为提高分布式业务系统一致性的分布式任务重试平台 <br/>
> ✅️ 支持秒级、可中断、可编排的高性能分布式任务调度平台
</p>

# 简介

> SnailJob 是一个灵活、可靠且高效的分布式任务重试和任务调度平台。其核心采用分区模式实现，具备高度可伸缩性和容错性的分布式系统。拥有完善的权限管理、强大的告警监控功能和友好的界面交互。欢迎大家接入并使用。

## snail-job-python

snail-job 项目的 python 客户端。[snail-job项目 java 后端](https://gitee.com/aizuda/snail-job)

Snail Job Python客户端主打的是“原汁原昧”, 无需嵌套在其他语言环境中; 具备与SnailJob的Java客户端Job模块一样的能力包括(集群、广播、静态分片、Map、MapReuce、DAG工作流、实时日志等功能)，而 `xxl-job`、`PowerJob` 等其他的任务调度系统都是通过 Java 客户端使用 `Runtime` 执行 `Python` 脚本, 那么会有如下几个问题：

1. 需要运行在Java环境中,即耗内存和又显得笨重
2. 不方便编写复杂的 Python 脚本
3. Java 客户端通过 Python 命令执行脚本，需要系统全局安装脚本的第三方依赖
4. 代码可维护性和可调试比较差

Snail Job Python 客户端可以直接对接 SnailJob 服务器，实现定时任务调度，并上报日志。Python 客户端当前仍不支持`重试任务`，也没有支持计划。

## 开始使用

### 基于源码开发

```shell
git clone https://gitee.com/opensnail/snail-job-python.git && cd snail-job-python
# 参考项目的 .env.example 文件创建 .env
cp .env.example .env
# 安装依赖
pip install -e .
# 参考 example 目录示例程序编写客户端业务代码
cd example/
# 启动程序
python main.py
```

> tip: 可以使用 uv run --with 的方式运行:
>
> `uv run --with=snail-job-python main.py`

登录后台，能看到对应host-id 为 `py-xxxxxx` 的客户端

**注意: snail-job-python 支持 `pip` 包安装，包名为`snail-job-python`**

### 示例

#### 定时任务

```python
from snailjob import *

@job("testJobExecutor")                                   # 1. testJobExecutor 为执行器名称
def test_job_executor(args: JobArgs) -> ExecuteResult:
    SnailLog.REMOTE.info(f"job_params: {args.job_params}")
    return ExecuteResult.success()                       # 2. 返回执行结果

if __name__ == "__main__":
    ExecutorManager.register(test_job_executor)           # 3. 注册执行器
    client_main()                                         # 4. 执行客户端主函数
```

新建定时任务, 执行器类型选择【Python】，执行器名称填入【testJobExecutor】

#### 动态分片

```python
from snailjob import *

testMyMapExecutor = MapExecutor("testMyMapExecutor")     # 1. 定义 MapExecutor 变量

@testMyMapExecutor.map()                                 # 2. 定义 ROOT_MAP 阶段任务
def testMyMapExecutor_rootMap(args: MapArgs):
    assert args.task_name == ROOT_MAP
    return mr_do_map(["1", "2", "3", "4"], "TWO_MAP")


@testMyMapExecutor.map("TWO_MAP")                        # 3. 定义 TWO_MAP 阶段任务
def testMyMapExecutor_twoMap(args: MapArgs):
    return ExecuteResult.success(args.map_result)


if __name__ == "__main__":
    ExecutorManager.register(testMyMapExecutor)          # 4. 注册执行器
    client_main()     
```

#### MapReduce

```python
from snailjob import *

testMapReduceJobExecutor = MapReduceExecutor("testMapReduceJobExecutor")  # 1. 定义 MapReduceExecutor 变量


@testMapReduceJobExecutor.map()                                           # 2. 定义 ROOT_MAP 阶段任务
def testMapReduceJobExecutor_rootMap(args: MapArgs):
    return mr_do_map(["1", "2", "3", "4", "5", "6"], "MONTH_MAP")         # 3. 上报分片信息


@testMapReduceJobExecutor.map("MONTH_MAP")                                # 4. 定义 ROOT_MAP 阶段任务
def testMapReduceJobExecutor_monthMap(args: MapArgs):
    return ExecuteResult.success(int(args.map_result) * 2)


@testMapReduceJobExecutor.reduce()                                        # 5. 定义 reduce 阶段任务
def testMapReduceJobExecutor_reduce(args: ReduceArgs):
    return ExecuteResult.success(sum([int(x) for x in args.map_result]))


@testMapReduceJobExecutor.merge()                                         # 6. 定义 merge 阶段任务
def testMapReduceJobExecutor_merge(args: MergeReduceArgs):
    return ExecuteResult.success(sum([int(x) for x in args.reduces]))


if __name__ == "__main__":
    ExecutorManager.register(testMapReduceJobExecutor)                    # 7. 注册执行器
    client_main()   
```

#### 响应停止事件

```python
@job("testJobExecutor")
def test_job_executor(args: JobArgs) -> ExecuteResult:
    for i in range(40):
        if ThreadPoolCache.event_is_set(args.task_batch_id):  # 1. 判断当前任务批次是否被终止
            SnailLog.REMOTE.info("任务已经被中断，立即返回")
            return ExecuteResult.failure()
        time.sleep(1)

    return ExecuteResult.success()
```

#### 工作流、静态分片与普通定时任务类似，不做赘述

### gRPC

开发者工具

```shell
python -m grpc_tools.protoc \
    --python_out=. \
    --grpc_python_out=. \
    --proto_path=. \
    snailjob/grpc/snailjob.proto
```

### Docker 开发环境

详见 `Dockerfile.dev` 文件

## 配置

详见 [CONFIGURATION.md](CONFIGURATION.md)

## Change Log

详见 [CHANGELOG.md](CHANGELOG.md)
