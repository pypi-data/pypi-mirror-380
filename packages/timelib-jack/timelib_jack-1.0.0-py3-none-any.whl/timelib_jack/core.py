from __future__ import annotations
import asyncio
import datetime, hashlib, traceback
from typing import Callable, Optional, List
from .utils import TimeUtils
from .logger import get_logger

logger = get_logger()

class AsyncJob:
    """
    تمثل مهمة واحدة داخل Scheduler.
    تدعم:
    - تنفيذ مرة واحدة
    - مهام دورية
    - cron-like
    - retry
    - priority
    - pause/resume/cancel
    """
    def __init__(self, func: Callable, run_at: datetime.datetime = None,
                 interval: Optional[float] = None,
                 args=(), kwargs=None, priority:int=5,
                 retry:int=0, retry_interval:float=1.0, cron: Optional[str]=None):
        self.func = func
        self.run_at = run_at
        self.interval = interval
        self.args = args
        self.kwargs = kwargs or {}
        self.priority = priority
        self.retry = retry
        self.retry_interval = retry_interval
        self.cron = cron
        self._paused = False
        self._cancelled = False

    def pause(self):
        """إيقاف المهمة مؤقتًا"""
        self._paused = True
        logger.info(f"Job {self.func.__name__} paused")

    def resume(self):
        """استئناف المهمة بعد الإيقاف المؤقت"""
        self._paused = False
        logger.info(f"Job {self.func.__name__} resumed")

    def cancel(self):
        """إلغاء المهمة نهائيًا"""
        self._cancelled = True
        logger.info(f"Job {self.func.__name__} cancelled")

    def next_run(self):
        """احسب الوقت القادم لتنفيذ المهمة"""
        if self._cancelled:
            return None
        if self.cron:
            return TimeUtils.next_cron(self.cron)
        elif self.run_at:
            return self.run_at
        else:
            return datetime.datetime.now()

class AsyncScheduler:
    """
    Scheduler رئيسي لتنفيذ المهام:
    - Async-ready
    - Cron-like
    - Retry + priority
    - حماية من تعديل الوقت
    """
    def __init__(self, tz: Optional[str]=None):
        self.jobs: List[AsyncJob] = []
        self._stop_flag = False
        self._time_hash = TimeUtils.compute_time_hash(tz)

    def add_job(self, func: Callable, run_at: datetime.datetime=None,
                interval: Optional[float]=None, args=(), kwargs=None,
                priority:int=5, retry:int=0, retry_interval:float=1.0,
                cron: Optional[str]=None):
        job = AsyncJob(func, run_at, interval, args, kwargs, priority,
                       retry, retry_interval, cron)
        self.jobs.append(job)
        logger.info(f"Added job {func.__name__}")
        return job

    async def _run_job(self, job: AsyncJob):
        """تنفيذ مهمة واحدة مع retry ودعم async"""
        attempt = 0
        while not job._cancelled:
            if job._paused:
                await asyncio.sleep(0.5)
                continue
            try:
                result = job.func(*job.args, **job.kwargs)
                if asyncio.iscoroutine(result):
                    await result
                break
            except Exception:
                attempt += 1
                logger.error(f"Job {job.func.__name__} failed attempt {attempt}:\n{traceback.format_exc()}")
                if attempt > job.retry:
                    break
                await asyncio.sleep(job.retry_interval)

    async def run(self):
        """حلقة التشغيل الرئيسية لكل المهام"""
        while not self._stop_flag:
            TimeUtils.check_time_integrity(self._time_hash)
            now = datetime.datetime.now()
            to_run = [job for job in self.jobs if job.next_run() and job.next_run() <= now]
            for job in sorted(to_run, key=lambda x: -x.priority):
                asyncio.create_task(self._run_job(job))
                if job.interval:
                    job.run_at = now + datetime.timedelta(seconds=job.interval)
                elif job.cron:
                    job.run_at = job.next_run()
                else:
                    self.jobs.remove(job)
            await asyncio.sleep(0.05)

    def stop(self):
        self._stop_flag = True
        logger.info("Stopping scheduler gracefully...")

    def list_jobs(self):
        for j in self.jobs:
            logger.info(f"Job {j.func.__name__}, next run: {j.next_run()}, interval: {j.interval}, cron: {j.cron}, priority: {j.priority}")