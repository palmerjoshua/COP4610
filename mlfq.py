"""
Joshua Palmer    Z: 23280034
COP 4610 001
Unit 6 CPU Scheduler Assignment
27 September 2015

github.com/palmerjoshua/COP4610
"""
from collections import deque

class MLFQ(deque):
    def __init__(self, priority, time_quantum=None, iterable=()):
        deque.__init__(self, iterable=iterable)
        self.priority = priority
        self.time_quantum = time_quantum

    def empty(self):
        return len(self) == 0
