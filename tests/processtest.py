from process import Process
from rawdata import RawData
import unittest, random


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


    def test_burst(self):
        expected_burst = sum(i for i in self.process.schedule['cpu'])
        actual_burst = 0
        while not self.process.is_done():
            current_burst = random.randrange(1, self.process.schedule['cpu'][0]+1)
            actual_burst += self.process.burst(amount=current_burst)
        self.assertEqual(expected_burst, actual_burst)
