from apscheduler.schedulers.asyncio import AsyncIOScheduler


class Scheduler:
    def __init__(self):
        self._scheduler = AsyncIOScheduler()
        self._scheduler.start()

    def add_job(self, func, *args, **kwargs):
        self._scheduler.add_job(func=func, args=args, kwargs=kwargs)


scheduler = Scheduler()
