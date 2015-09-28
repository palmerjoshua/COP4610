"""
Joshua Palmer    Z: 23280034
COP 4610 001
Unit 6 CPU Scheduler Assignment
27 September 2015

github.com/palmerjoshua/COP4610
"""
class RawData:
    def __init__(self):
        """Contains the CPU burst times and I/O times
        for the processes given in the assignment guidelines.
        This class provides a simple interface between a Process
        object and the data it's supposed to have."""
        self.p1 = [7, 19, 8, 13, 17, 13, 19, 19, 44, 15, 29, 51, 14, 68, 15, 49, 14]
        self.p2 = [9, 52, 12, 42, 24, 31, 24, 21, 26, 43, 14, 31, 23, 32, 15]
        self.p3 = [25, 51, 43, 53, 44, 21, 15, 31, 24, 29, 31, 34, 12]
        self.p4 = [6, 29, 5, 22, 6, 24, 8, 27, 5, 25, 6, 24, 8, 26, 9, 22, 8]
        self.p5 = [5, 66, 6, 82, 5, 71, 6, 43, 4, 26, 6, 51, 3, 77, 4, 61, 3, 42, 5]
        self.p6 = [9, 35, 8, 41, 11, 33, 13, 32, 8, 41, 16, 29, 11]
        self.p7 = [5, 28, 6, 21, 5, 39, 8, 16, 7, 29, 5, 31, 4, 22, 6, 24, 5]
        self.p8 = [20, 26, 19, 23, 18, 42, 27, 43, 19, 37, 26, 43, 35, 55, 21]
        self.p9 = [6, 35, 5, 41, 6, 33, 4, 32, 8, 31, 4, 29, 5, 16, 3, 32, 4]

    def process_list(self):
        """Generates a 2-dimensional list of the raw process data
        :returns list of process data
        :rtype list of list of int"""
        return [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8, self.p9]

    def process_dict(self):
        """Generates a dictionary of the raw process data
        :returns raw data in dictionary format
        :rtype dict (key=str, val=list of int)"""
        return {'p{}'.format(i+1): p for i, p in enumerate(self.process_list())}
