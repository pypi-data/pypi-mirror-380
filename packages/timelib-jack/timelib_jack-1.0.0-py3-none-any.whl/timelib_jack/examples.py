import asyncio
import datetime
from .core import AsyncScheduler

async def main():
    scheduler = AsyncScheduler()

    # مثال: مهمة دورية كل 5 ثواني
    def task1():
        print("Task 1 executed:", datetime.datetime.now())

    scheduler.add_job(task1, interval=5)

    # مثال: مهمة cron كل دقيقة
    def task2():
        print("Task 2 cron executed:", datetime.datetime.now())

    scheduler.add_job(task2, cron="* * * * *")

    # مثال: إيقاف البرنامج بعد 30 ثانية
    async def stop_scheduler_later():
        await asyncio.sleep(30)
        scheduler.stop()

    asyncio.create_task(stop_scheduler_later())

    # تشغيل scheduler
    await scheduler.run()

if __name__ == "__main__":
    asyncio.run(main())