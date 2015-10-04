"""
Joshua Palmer    Z: 23280034
COP 4610 001
Unit 6 CPU Scheduler Assignment
27 September 2015

github.com/palmerjoshua/COP4610
"""

class Process:
    def __init__(self, number, arrival_time=0, burst_time=0, raw_list=None):
        """Represents a Process that will run on the CPU.
        :param number unique identifier
        :type number int
        """
        self.number = number
        self.schedule = {
            'cpu': raw_list[0::2] if raw_list else [],
            'io': raw_list[1::2] if raw_list else []}
        self.burst_time = self.current_burst_time = burst_time
        self.arrival_time = self.current_arrival_time = arrival_time


    def is_done(self):
        return (not self.schedule['cpu'] and not self.schedule['io']) or \
               (all(i == 0 for i in self.schedule['cpu']) and all(i == 0 for i in self.schedule['io']))

    def burst(self, amount=None):
        """Changes the attributes of the Process based
        on its CPU burst.
        :param amount the length of the CPU burst.
        :type amount int
        """
        current = self.current_burst_time - amount
        self.current_burst_time = current if current >= 0 else 0
        self.current_arrival_time += amount
        # todo fully implement burst algorithm
