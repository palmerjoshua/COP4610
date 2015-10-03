from process import Process
from rawdata import RawData
import unittest

class ProcessTest(unittest.TestCase):
    def setUp(self):
        self.process = Process(0)
        self.raw_data = RawData()


    def test_import_raw(self):
        self.process.import_raw(self.raw_data.p1)
        cpu, io = self.raw_data.p1[::2], self.raw_data.p1[1::2]
        pcpu, pio = self.process.schedule['cpu'], self.process.schedule['io']
        self.assertTrue(cpu==pcpu and io==pio, "should be equal")
