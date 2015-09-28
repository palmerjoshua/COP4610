"""
Joshua Palmer    Z: 23280034
COP 4610 001
Unit 6 CPU Scheduler Assignment
27 September 2015

github.com/palmerjoshua/COP4610
"""
from queue import Queue

class MLFQ(Queue):
    def __init__(self, priority, time_quantum, max_size=0):
        """Same as a Queue, but also has a priority and a time quantum.
        :param priority The scheduling priority of the items in the queue
        :type priority int
        :param time_quantum The time quantum used for the RR algorithm
        :type time_quantum int"""
        Queue.__init__(self, maxsize=max_size)
        self.priority = priority
        self.time_quantum = time_quantum
