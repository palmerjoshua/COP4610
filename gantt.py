from collections import OrderedDict
class GanttChart:

    def __init__(self, algorithm_name):
        self.algorithm_name = algorithm_name
        self.blocks = []

    def new_block(self, process_number, start_time, burst_amount):
        return {'start_time': start_time,
                'process_number': process_number,
                'burst_amount': burst_amount,
                'end_time': start_time + burst_amount}

    def add_block(self, process_number, start_time, burst_amount):
        self.blocks.append(self.new_block(process_number, start_time, burst_amount))

    def get_chart(self):
        chart = ""
        for i, block in enumerate(self.blocks):
            print("{:>4} P{} {:<4}".format(block['start_time'], block['process_number'], block['end_time']))
        return chart.rstrip(' ')

