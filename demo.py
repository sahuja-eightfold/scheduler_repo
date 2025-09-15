import time
from scheduler import Scheduler

def hello():
    print("Hello, world!")

def recurring_task():
    print("Recurring task running...")

if __name__ == "__main__":
    s = Scheduler()
    s.schedule("task1", 2000, hello)
    s.schedule("task2", 1000, recurring_task, recurring=True, interval_ms=1000)

    time.sleep(5)
    s.cancel("task2")
    print("Cancelled recurring task.")
    time.sleep(2)
    s.shutdown()
    print("Scheduler shutdown complete.")
