"""
Joshua Palmer    Z: 23280034
COP 4610 001
Unit 6 CPU Scheduler Assignment
27 September 2015

github.com/palmerjoshua/COP4610
"""
from mlfq import MLFQ
from gantt import GanttChart

from queue import Queue
class Scheduler:
    def __init__(self, algorithm_name, processes=None):
        """Scheduler parent class
        :param processes list of Process objects
        """
        self.processes = processes or []
        self.finished = []
        self.current_time = 0
        self.chart = GanttChart(algorithm_name)

    def done(self):
        return self.finished and not self.processes

    def run(self):
        pass


class FCFSScheduler(Scheduler):
    def __init__(self, processes):
        """First come first serve scheduler
        :param processes List of processes that will be scheduled.
        :type processes list of Process
        """
        Scheduler.__init__(self, 'FCFS', processes)

    def run(self):
        while not self.done():

            start = self.current_time

            current_process = min(self.processes, key=lambda p: p.arrival_time)
            #print("Current Process: P{}".format(current_process.number))
            burst_amount = current_process.burst(start_time=self.current_time)
            self.current_time += burst_amount
            self.chart.add_block(current_process.number, start, self.current_time)
            #print("Current Time: {}".format(self.current_time))
            if current_process.is_done():
                self.finished.append(current_process)
                self.processes.remove(current_process)
        print(self.chart.get_chart())
        pass


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

def main():
    from rawdata import RawData
    from process import Process
    processes = [Process(i+1, raw_list=plist) for i, plist in enumerate(RawData().process_list())]
    scheduler = FCFSScheduler(processes)
    scheduler.run()
    print("Ending time: {}".format(scheduler.current_time))

if __name__ == '__main__':
    main()
