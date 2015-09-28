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
        self.schedule = {'cpu': [], 'io': []}
        self.current_burst_time = burst_time
        self.current_arrival_time = arrival_time
        if raw_list:
            self.import_raw(raw_list)

    def import_raw(self, raw_list):
        """Turns a list of raw data into a schedule dictionary.
        :param raw_list list of raw data
        :type raw_list list of int
        """
        for i, item in enumerate(raw_list):
            target = 'io' if i % 2 else 'cpu'
            self.schedule[target].append(item)

    def burst(self, amount):
        """Changes the attributes of the Process based
        on its CPU burst.
        :param amount the length of the CPU burst.
        :type amount int
        """
        current = self.current_burst_time - amount
        self.current_burst_time = current if current >= 0 else 0
        self.current_arrival_time += amount
        # todo fully implement burst algorithm
