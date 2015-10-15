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
            chart += "{:<4} P{} ".format(block['start_time'], block['process_number'])

            if i == len(self.blocks)-1:
                chart += " {:>4}".format(block['end_time'])
            elif i > 0 and i % 8 == 0:
                chart += "\n"
        return chart.rstrip(' ')

