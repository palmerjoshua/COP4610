from process import Process
from rawdata import RawData
import unittest

class ProcessTest(unittest.TestCase):
    def setUp(self):
        self.raw_data = RawData().p1
        self.process = Process(0, self.raw_data)



    def test_is_done(self):
        while not self.process.is_done():
            self.process.schedule['cpu'].pop()
            self.process.schedule['io'].pop()
        valid = not self.process.schedule['cpu'] and not self.process.schedule['io']
        self.assertTrue(valid and self.process.is_done())
