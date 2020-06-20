import asyncio


class MotorManager:
    def __init__(self):
        pass

    def create_task(self, time, callback):
        bg_task = BackgroundTask()

        asyncio.run(bg_task.run(self.run_motor, (time,), callback))

    @asyncio.coroutine
    def run_motor(self, time):
        # TODO: Turn on the motor
        print('Motor on')
        yield from asyncio.sleep(time)
        print('Motor off')


class BackgroundTask:
    async def run(self, coro, args, callback=None):
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, self.task_runner, coro, args, callback)

    def task_runner(self, coro, args, callback):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        fut = asyncio.ensure_future(coro(*args))
        if callback is not None:
            fut.add_done_callback(callback)

        loop.run_until_complete(fut)
        loop.close()
