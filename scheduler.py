"""
Joshua Palmer    Z: 23280034
COP 4610 001
Unit 6 CPU Scheduler Assignment
27 September 2015

github.com/palmerjoshua/COP4610
"""
from mlfq import MLFQ

class Scheduler:
    def __init__(self, processes=None):
        """Scheduler parent class
        :param processes list of Process objects
        """
        self.processes = processes or []


class FCFSScheduler(Scheduler):
    def __init__(self, processes):
        """First come first serve scheduler
        :param processes List of processes that will be scheduled.
        :type processes list of Process
        """
        Scheduler.__init__(self, processes)


class MLFQScheduler(Scheduler):
    def __init__(self, processes, *priority_timeq):
        """Multi-level feedback queue scheduler
        :param processes list of processes to be scheduled
        :type processes list of Process
        :param priority_timeq contains the priority and
                time quantum for each queue in the system.
        :type priority_timeq tuple (one per queue)
        """
        Scheduler.__init__(self, processes)
        self.queues = self.init_queues(priority_timeq) if priority_timeq else {}

    def init_queues(self, *queue_data):
        """creates a dictionary of MLFQ based on the given priorities/time quantums
        :param queue_data a tuple for each MLFQ
        :raises ValueError if queue data is anything but tuples"""
        if all(type(d) is tuple for d in queue_data):
            for i, (priority, time_quantum) in enumerate(queue_data):
                key = "q{num}".format(num=i+1)
                self.queues[key] = MLFQ(priority, time_quantum)
        else:
            raise ValueError("queue_data must be tuples")
