"""
Joshua Palmer    Z: 23280034
COP 4610 001
Unit 6 CPU Scheduler Assignment
27 September 2015

github.com/palmerjoshua/COP4610
"""

class Process:
    def __init__(self, process_number, arrival_time=0, raw_list=None):
        """Represents a Process that will run on the CPU.
        :param process_number unique identifier
        :type process_number int
        """
        self.number = process_number
        self.schedule = {
            'cpu': raw_list[0::2] if raw_list else [],
            'io': raw_list[1::2] if raw_list else []
        }
        self.arrival_time = arrival_time
        self.wait_time = 0
        self.work_time = 0
        self.turnaround_time = 0
        self.response_time = 0

    def is_done(self):
        return len(self.schedule['cpu']) == 0

    def _calculate_stats(self, start_time, burst_amount):
        if self.response_time == 0:
            self.response_time = start_time - self.arrival_time
        self.work_time += burst_amount
        self.wait_time += (start_time - self.arrival_time)
        self.turnaround_time = self.wait_time + self.work_time
        io_time = self.schedule['io'].pop(0) if self.schedule['io'] else 0
        self.arrival_time = start_time + burst_amount + io_time

    def _get_burst(self, amount):
        if not amount:
            total_burst = self.schedule['cpu'].pop(0)
        else:
            total_burst = 0
            current_burst = self.schedule['cpu'][0]
            amount = amount or current_burst
            for i in range(amount):
                total_burst += 1
                current_burst -= 1
                if not current_burst:
                    break
            if current_burst <= 0:
                self.schedule['cpu'] = self.schedule['cpu'][1:]
        return total_burst

    def burst(self, amount=0, start_time=0):
        """Changes the attributes of the Process based
        on its CPU burst.
        :param amount the length of the CPU burst.
        :type amount int
        """
        if not self.schedule['cpu']:
            return 0
        total_burst = self._get_burst(amount)
        self._calculate_stats(start_time, total_burst)
        return total_burst

