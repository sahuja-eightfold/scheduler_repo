import time
import threading

class Scheduler:
    def __init__(self):
        self.tasks = {}
        self.lock = threading.Lock()

    def schedule(self, task_id, delay_ms, func, recurring=False, interval_ms=None):
        if task_id in self.tasks:
            raise ValueError(f"Task {task_id} already exists.")

        def wrapper():
            if recurring:
                while task_id in self.tasks:
                    time.sleep(interval_ms / 1000.0)
                    try:
                        func()
                    except Exception as e:
                        print(f"Error executing task {task_id}: {e}")
            else:
                time.sleep(delay_ms / 1000.0)
                if task_id in self.tasks:
                    try:
                        func()
                    except Exception as e:
                        print(f"Error executing task {task_id}: {e}")
                    self.cancel(task_id)

        thread = threading.Thread(target=wrapper, daemon=True)
        with self.lock:
            self.tasks[task_id] = thread
        thread.start()

    def cancel(self, task_id):
        with self.lock:
            if task_id in self.tasks:
                del self.tasks[task_id]

    def shutdown(self):
        with self.lock:
            self.tasks.clear()
