#!/usr/bin/env python3
"""
定时任务调度器

提供定时任务管理功能，支持cron表达式和间隔执行
"""

import asyncio
import threading
import time
from datetime import datetime, timedelta
from typing import Callable, Optional, Dict, Any, List, Union
from enum import Enum
import uuid
from dataclasses import dataclass
from functools import wraps

from pyadvincekit.logging import get_logger
from pyadvincekit.core.trace import TraceContext, get_current_trace_id

logger = get_logger(__name__)


class TaskStatus(Enum):
    """任务状态"""
    PENDING = "pending"      # 等待执行
    RUNNING = "running"      # 正在执行
    COMPLETED = "completed"  # 执行完成
    FAILED = "failed"        # 执行失败
    CANCELLED = "cancelled"   # 已取消


class TaskType(Enum):
    """任务类型"""
    ONCE = "once"           # 一次性任务
    INTERVAL = "interval"   # 间隔任务
    CRON = "cron"          # Cron表达式任务


@dataclass
class TaskInfo:
    """任务信息"""
    task_id: str
    name: str
    func: Callable
    args: tuple
    kwargs: dict
    task_type: TaskType
    status: TaskStatus = TaskStatus.PENDING
    created_at: datetime = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    next_run: Optional[datetime] = None
    interval_seconds: Optional[int] = None
    cron_expression: Optional[str] = None
    max_retries: int = 3
    retry_count: int = 0
    error_message: Optional[str] = None
    trace_id: Optional[str] = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()


class TaskScheduler:
    """任务调度器"""
    
    def __init__(self):
        self.tasks: Dict[str, TaskInfo] = {}
        self.running = False
        self._scheduler_thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        self._lock = threading.Lock()
    
    def add_task(
        self,
        func: Callable,
        name: Optional[str] = None,
        args: tuple = (),
        kwargs: dict = None,
        task_type: TaskType = TaskType.ONCE,
        interval_seconds: Optional[int] = None,
        cron_expression: Optional[str] = None,
        max_retries: int = 3,
        trace_id: Optional[str] = None
    ) -> str:
        """添加任务"""
        if kwargs is None:
            kwargs = {}
        
        task_id = str(uuid.uuid4())
        task_name = name or f"{func.__name__}_{task_id[:8]}"
        
        # 计算下次执行时间
        next_run = None
        if task_type == TaskType.INTERVAL and interval_seconds:
            next_run = datetime.now() + timedelta(seconds=interval_seconds)
        elif task_type == TaskType.CRON and cron_expression:
            # 这里可以集成cron解析库，暂时使用简单实现
            next_run = datetime.now() + timedelta(minutes=1)
        elif task_type == TaskType.ONCE:
            next_run = datetime.now()
        
        task_info = TaskInfo(
            task_id=task_id,
            name=task_name,
            func=func,
            args=args,
            kwargs=kwargs,
            task_type=task_type,
            interval_seconds=interval_seconds,
            cron_expression=cron_expression,
            max_retries=max_retries,
            trace_id=trace_id or get_current_trace_id()
        )
        task_info.next_run = next_run
        
        with self._lock:
            self.tasks[task_id] = task_info
        
        logger.info(f"Task added: {task_name} (ID: {task_id})")
        return task_id
    
    def remove_task(self, task_id: str) -> bool:
        """移除任务"""
        with self._lock:
            if task_id in self.tasks:
                task = self.tasks[task_id]
                if task.status == TaskStatus.RUNNING:
                    logger.warning(f"Cannot remove running task: {task.name}")
                    return False
                
                del self.tasks[task_id]
                logger.info(f"Task removed: {task.name} (ID: {task_id})")
                return True
            return False
    
    def get_task(self, task_id: str) -> Optional[TaskInfo]:
        """获取任务信息"""
        with self._lock:
            return self.tasks.get(task_id)
    
    def list_tasks(self, status: Optional[TaskStatus] = None) -> List[TaskInfo]:
        """列出任务"""
        with self._lock:
            tasks = list(self.tasks.values())
            if status:
                tasks = [task for task in tasks if task.status == status]
            return tasks
    
    def start(self):
        """启动调度器"""
        if self.running:
            logger.warning("Scheduler is already running")
            return
        
        self.running = True
        self._stop_event.clear()
        self._scheduler_thread = threading.Thread(target=self._scheduler_loop, daemon=True)
        self._scheduler_thread.start()
        logger.info("Task scheduler started")
    
    def stop(self):
        """停止调度器"""
        if not self.running:
            logger.warning("Scheduler is not running")
            return
        
        self.running = False
        self._stop_event.set()
        
        if self._scheduler_thread:
            self._scheduler_thread.join(timeout=5)
        
        logger.info("Task scheduler stopped")
    
    def _scheduler_loop(self):
        """调度器主循环"""
        while self.running and not self._stop_event.is_set():
            try:
                current_time = datetime.now()
                tasks_to_run = []
                
                with self._lock:
                    for task in self.tasks.values():
                        if (task.status == TaskStatus.PENDING and 
                            task.next_run and 
                            task.next_run <= current_time):
                            tasks_to_run.append(task)
                
                # 执行任务
                for task in tasks_to_run:
                    self._execute_task(task)
                
                # 休眠1秒
                time.sleep(1)
                
            except Exception as e:
                logger.error(f"Scheduler loop error: {e}")
                time.sleep(1)
    
    def _execute_task(self, task: TaskInfo):
        """执行任务"""
        task.status = TaskStatus.RUNNING
        task.started_at = datetime.now()
        task.retry_count += 1
        
        logger.info(f"Executing task: {task.name} (ID: {task.task_id})")
        
        try:
            # 在跟踪上下文中执行任务
            with TraceContext(
                trace_id=task.trace_id,
                user_id="scheduler",
                request_id=f"task_{task.task_id}"
            ):
                if asyncio.iscoroutinefunction(task.func):
                    # 异步函数
                    asyncio.run(task.func(*task.args, **task.kwargs))
                else:
                    # 同步函数
                    task.func(*task.args, **task.kwargs)
            
            task.status = TaskStatus.COMPLETED
            task.completed_at = datetime.now()
            logger.info(f"Task completed: {task.name} (ID: {task.task_id})")
            
            # 如果是间隔任务，计算下次执行时间
            if task.task_type == TaskType.INTERVAL and task.interval_seconds:
                task.next_run = datetime.now() + timedelta(seconds=task.interval_seconds)
                task.status = TaskStatus.PENDING
                logger.info(f"Task scheduled for next run: {task.next_run}")
            
        except Exception as e:
            task.error_message = str(e)
            logger.error(f"Task failed: {task.name} (ID: {task.task_id}) - {e}")
            
            if task.retry_count < task.max_retries:
                # 重试
                task.status = TaskStatus.PENDING
                task.next_run = datetime.now() + timedelta(seconds=60)  # 1分钟后重试
                logger.info(f"Task will retry: {task.name} (retry {task.retry_count}/{task.max_retries})")
            else:
                # 达到最大重试次数
                task.status = TaskStatus.FAILED
                logger.error(f"Task failed permanently: {task.name} (ID: {task.task_id})")


# 全局调度器实例
_scheduler: Optional[TaskScheduler] = None


def get_scheduler() -> TaskScheduler:
    """获取全局调度器实例"""
    global _scheduler
    if _scheduler is None:
        _scheduler = TaskScheduler()
    return _scheduler


def schedule_task(
    func: Callable,
    name: Optional[str] = None,
    args: tuple = (),
    kwargs: dict = None,
    task_type: TaskType = TaskType.ONCE,
    interval_seconds: Optional[int] = None,
    cron_expression: Optional[str] = None,
    max_retries: int = 3
) -> str:
    """调度任务"""
    scheduler = get_scheduler()
    return scheduler.add_task(
        func=func,
        name=name,
        args=args,
        kwargs=kwargs,
        task_type=task_type,
        interval_seconds=interval_seconds,
        cron_expression=cron_expression,
        max_retries=max_retries
    )


def schedule_once(
    func: Callable,
    name: Optional[str] = None,
    args: tuple = (),
    kwargs: dict = None,
    max_retries: int = 3
) -> str:
    """调度一次性任务"""
    return schedule_task(
        func=func,
        name=name,
        args=args,
        kwargs=kwargs,
        task_type=TaskType.ONCE,
        max_retries=max_retries
    )


def schedule_interval(
    func: Callable,
    interval_seconds: int,
    name: Optional[str] = None,
    args: tuple = (),
    kwargs: dict = None,
    max_retries: int = 3
) -> str:
    """调度间隔任务"""
    return schedule_task(
        func=func,
        name=name,
        args=args,
        kwargs=kwargs,
        task_type=TaskType.INTERVAL,
        interval_seconds=interval_seconds,
        max_retries=max_retries
    )


def schedule_cron(
    func: Callable,
    cron_expression: str,
    name: Optional[str] = None,
    args: tuple = (),
    kwargs: dict = None,
    max_retries: int = 3
) -> str:
    """调度Cron任务"""
    return schedule_task(
        func=func,
        name=name,
        args=args,
        kwargs=kwargs,
        task_type=TaskType.CRON,
        cron_expression=cron_expression,
        max_retries=max_retries
    )


def start_scheduler():
    """启动调度器"""
    scheduler = get_scheduler()
    scheduler.start()


def stop_scheduler():
    """停止调度器"""
    scheduler = get_scheduler()
    scheduler.stop()


def get_task_status(task_id: str) -> Optional[TaskStatus]:
    """获取任务状态"""
    scheduler = get_scheduler()
    task = scheduler.get_task(task_id)
    return task.status if task else None


def list_tasks(status: Optional[TaskStatus] = None) -> List[TaskInfo]:
    """列出任务"""
    scheduler = get_scheduler()
    return scheduler.list_tasks(status)


def remove_task(task_id: str) -> bool:
    """移除任务"""
    scheduler = get_scheduler()
    return scheduler.remove_task(task_id)


# 装饰器
def scheduled_task(
    name: Optional[str] = None,
    task_type: TaskType = TaskType.ONCE,
    interval_seconds: Optional[int] = None,
    cron_expression: Optional[str] = None,
    max_retries: int = 3
):
    """任务装饰器"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        
        # 注册任务
        schedule_task(
            func=func,
            name=name or func.__name__,
            task_type=task_type,
            interval_seconds=interval_seconds,
            cron_expression=cron_expression,
            max_retries=max_retries
        )
        
        return wrapper
    return decorator


def interval_task(seconds: int, name: Optional[str] = None, max_retries: int = 3):
    """间隔任务装饰器"""
    return scheduled_task(
        name=name,
        task_type=TaskType.INTERVAL,
        interval_seconds=seconds,
        max_retries=max_retries
    )


def cron_task(cron_expression: str, name: Optional[str] = None, max_retries: int = 3):
    """Cron任务装饰器"""
    return scheduled_task(
        name=name,
        task_type=TaskType.CRON,
        cron_expression=cron_expression,
        max_retries=max_retries
    )




