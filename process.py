class Process:
    def __init__(self, number, raw_list=None):
        self.number = number
        self.schedule = {'cpu': [], 'io': []}
        if raw_list:
            self.import_raw(raw_list)

    def import_raw(self, raw_list):
        for i, item in enumerate(raw_list):
            target = 'io' if i % 2 else 'cpu'
            self.schedule[target].append(item)
