import time
import unittest
from scheduler import Scheduler

class TestScheduler(unittest.TestCase):
    def test_one_time_task(self):
        s = Scheduler()
        result = []
        def task(): result.append("done")
        s.schedule("t1", 500, task)
        time.sleep(1)
        self.assertIn("done", result)

    def test_recurring_task(self):
        s = Scheduler()
        result = []
        def task(): result.append("tick")
        s.schedule("t2", 0, task, recurring=True, interval_ms=200)
        time.sleep(1)
        s.cancel("t2")
        self.assertGreaterEqual(len(result), 3)

    def test_cancel_task(self):
        s = Scheduler()
        result = []
        def task(): result.append("fail")
        s.schedule("t3", 1000, task)
        s.cancel("t3")
        time.sleep(1.5)
        self.assertNotIn("fail", result)

if __name__ == "__main__":
    unittest.main()
