import unittest
import scheduler
from process import Process
from rawdata import RawData

class MLFQTest(unittest.TestCase):
    def setUp(self):
        data = RawData().process_list()
        processes = [Process(i+1) for i, _ in enumerate(data)]
        for d, process in zip(data, processes):
            process.import_raw(d)
        self.sched = scheduler.MLFQScheduler(processes)

    def test_init_queues(self):
        self.sched.init_queues((1, 3), (2, 4))
        q1_exists = 'q1' in self.sched.queues
        q2_exists = 'q2' in self.sched.queues
        q1 = self.sched.queues['q1'] if q1_exists else None
        q2 = self.sched.queues['q2'] if q2_exists else None
        q1_good = (q1.priority == 1 and q1.time_quantum == 3) if q1 else False
        q2_good = (q2.priority == 2 and q2.time_quantum == 4) if q2 else False
        self.assertTrue(q1_good and q2_good, "Queues need to be initialized with priority and TQ")

    def test_init_queues_fail(self):
        self.assertRaises(ValueError, self.sched.init_queues, 1,2,3)
        pass