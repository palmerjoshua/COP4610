import unittest
from scheduler import MLFQScheduler
from process import Process
from rawdata import RawData

class MLFQSchedulerTest(unittest.TestCase):
    def setUp(self):
        data = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]]
        processes = [Process(i+1, raw_list=plist) for i, plist in enumerate(data)]
        self.scheduler = MLFQScheduler('mlfq', processes)