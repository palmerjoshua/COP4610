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


    def display(self, current_process):
        print("*" * 42)
        print("Current time:", self.current_time)
        print("Running: P{num}".format(num=current_process.number))
        #print("*" * 30)
        ready_q = [p for p in self.processes if p.number != current_process.number and p.arrival_time <= self.current_time]
        ready_q.sort(key=lambda p: p.arrival_time)
        if ready_q:
            print("Ready Queue:    Process              Burst")
        for p in ready_q:
            print("                     P{}                 {:>2}".format(p.number, p.get_next_burst()))
        in_io = [p for p in self.processes if p.number != current_process.number and p not in ready_q]
        in_io.sort(key=lambda p: p.arrival_time-self.current_time)
        if in_io:
            print("In I/O:         Process     Remaining Time")
        for p in in_io:
            print("                     P{}                 {:>2}".format(p.number, p.arrival_time - self.current_time))


    def run(self):
        while not self.done():
            current_process = min(self.processes, key=lambda p: p.arrival_time)
            self.display(current_process)
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
        #print(self.chart.get_chart())
        pass


class NoArrivalException(Exception):
    pass

class MLFQScheduler(Scheduler):
    def __init__(self, processes):
        Scheduler.__init__(self, processes)
        self.processes = processes
        self.queues = self._init_queues()


    def _init_queues(self):
        queues = OrderedDict()
        queues[1] = MLFQ(1, 6, self.processes)
        queues[2] = MLFQ(2, 12)
        queues[3] = MLFQ(3)
        return queues

    def done(self):
        return self.finished and all(q.empty() for q in self.queues.values())

    def _get_arrived(self, load_first=True):
        for q in self.queues.values():
            if q and self.current_time >= q[0].arrival_time:
                return q[0]
        pass
        raise NoArrivalException('No queue has an arrived process')

    def _add_to_queue(self, *procs):
        for p in procs:
            self.queues[p.priority].append(p)

    def do_io(self, current_number):
        procs = []
        for q in self.queues.values():
            for p in q:
                if p.number != current_number and p.in_io:
                    p.do_io(1)


    def run(self):
        while not self.done():
            try:
                current_proc = self._get_arrived()
            except NoArrivalException:
                self.current_time += 1
                continue
            else:
                if self.current_time == 976:
                    pass
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
                    current_proc.arrival_time = self.current_time
                    i += 1

                current_q.remove(current_proc)
                if current_proc.is_done():
                    self.finished.append(current_proc)
                elif potential_burst - total_burst <= 0:
                    io_time = current_proc.get_next_io(True) if (i==burst_limit and total_burst==potential_burst) else 0
                    current_proc.arrival_time = self.current_time + io_time
                    current_q.append(current_proc)
                else:

                    current_proc.priority += 1 if current_proc.priority < 3 else 0
                    #self.queues[current_proc.priority].append(current_proc)
                    self.ready_queue.append(current_proc)
                self.chart.add_block(current_proc.number, start, total_burst)
        print(self.chart.get_chart())


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
    display_fcfs_gantt_chart()
    #main()
