import asyncio
import time

NUMBER_OF_MOTORS = 2


class MotorManager:
    def __init__(self):
        self.motor_states = [False for x in range(NUMBER_OF_MOTORS)]
        self.bg_task = BackgroundTask()
        self.start_time = time.time()

    def create_task(self, motors, seconds, callback):
        longest_wait = max(seconds)
        self.start_time = time.time()

        for motor_n, state in enumerate(motors):
            cb = None
            if state is True:
                if seconds[motor_n] == longest_wait:
                    cb = callback
                self.motor_states[motor_n] = True
                asyncio.run(self.bg_task.run(self.run_motor, (motor_n, seconds[motor_n],), cb))
        self.update_serial()

    def update_serial(self):
        serial_str = ""
        for motor in self.motor_states:
            if motor:
                serial_str += "1 "
            else:
                serial_str += "0 "

        # TODO: Send to serial
        print(f"({round(time.time() - self.start_time, 1)})", serial_str)

    @asyncio.coroutine
    def run_motor(self, motor_n, seconds):
        yield from asyncio.sleep(seconds)
        self.motor_states[motor_n] = False
        self.update_serial()


class BackgroundTask:
    def __init__(self):
        self.loop = asyncio.get_event_loop()

    def get_loop(self):
        if self.loop.is_closed():
            self.loop = asyncio.get_event_loop()

    async def run(self, coro, args, callback=None):
        self.get_loop()
        self.loop.run_in_executor(None, self.task_runner, coro, args, callback)

    def task_runner(self, coro, args, callback):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        fut = asyncio.ensure_future(coro(*args))
        if callback is not None:
            fut.add_done_callback(callback)

        loop.run_until_complete(fut)
        loop.close()
