"""
Joshua Palmer    Z: 23280034
COP 4610 001
Unit 6 CPU Scheduler Assignment
27 September 2015

github.com/palmerjoshua/COP4610
"""
from mlfq import MLFQ
from gantt import GanttChart
from collections import deque, OrderedDict
from process import Process

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
            current_process = min(self.processes, key=lambda p: p.arrival_time)

            if self.current_time < current_process.arrival_time:
                self.current_time = current_process.arrival_time

            start = self.current_time
            burst_amount = current_process.burst(start_time=start)
            io_time = current_process.schedule['io'].pop(0) if current_process.schedule['io'] else 0
            current_process.arrival_time = start + burst_amount + io_time

            self.chart.add_block(current_process.number, self.current_time, burst_amount)

            self.current_time += burst_amount

            if current_process.is_done():
                self.finished.append(current_process)
                self.processes.remove(current_process)
        print(self.chart.get_chart())
        pass


class NoArrivalException(Exception):
    pass

class MLFQScheduler(Scheduler):
    def __init__(self, processes):
        Scheduler.__init__(self, processes)
        self.processes = processes
        self.queues = self._init_queues()
        self.ready_queue = deque()

    def _init_queues(self):
        queues = OrderedDict()
        queues[1] = MLFQ(1, 6, self.processes)
        queues[2] = MLFQ(2, 12)
        queues[3] = MLFQ(3)
        return queues

    def done(self):
        return self.finished and all(q.empty() for q in self.queues.values())

    def _get_arrived(self, load_first=True):
        if len(self.ready_queue) > 0 and load_first:
            self._load_ready_procs()
        for q in self.queues.values():
            if q and self.current_time >= q[0].arrival_time:
                return q[0]
        raise NoArrivalException('No queue has an arrived process')

    def _add_to_queue(self, *procs):
        for p in procs:
            self.queues[p.priority].append(p)

    def _load_ready_procs(self):
        to_deploy = [p for p in self.ready_queue if self.current_time >= p.arrival_time]
        for p in to_deploy:
            self.ready_queue.remove(p)
        self._add_to_queue(*to_deploy)


    def run(self):
        while not self.done():
            try:
                current_proc = self._get_arrived()
            except NoArrivalException:
                self.current_time += 1
                continue
            else:
                current_q = self.queues[current_proc.priority]
                burst_limit = current_q.time_quantum or current_proc.get_next_burst()
                potential_burst = current_proc.get_next_burst()
                i = 0
                start = self.current_time
                total_burst = 0
                while i < burst_limit and current_proc.equals(self._get_arrived()):
                    current_burst = current_proc.burst(amount=1, start_time=self.current_time)
                    total_burst += current_burst
                    self.current_time += current_burst
                    i += 1
                io_time = current_proc.get_next_io(True) if i == burst_limit else 0
                current_proc.arrival_time = self.current_time + io_time
                current_q.remove(current_proc)
                if current_proc.is_done():
                    self.finished.append(current_proc)
                elif i == burst_limit and potential_burst - total_burst <= 0:
                    current_q.append(current_proc)
                else:
                    self.ready_queue.append(current_proc)


def display_fcfs_gantt_chart():
    from rawdata import RawData
    processes = [Process(i+1, raw_list=plist) for i, plist in enumerate(RawData().process_list())]
    scheduler = FCFSScheduler(processes)
    scheduler.run()
    print("Ending time: {}".format(scheduler.current_time))

def main():
    from rawdata import RawData
    processes = [Process(i+1, raw_list=plist) for i, plist in enumerate(RawData().process_list())]
    sched = MLFQScheduler(processes)
    sched.run()
    print("Ending time: {}".format(sched.current_time))
if __name__ == '__main__':
    # display_fcfs_gantt_chart()
    main()
