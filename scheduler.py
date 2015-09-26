from queue import Queue

class Scheduler:
    def __init__(self, processes=None):
        self.processes = processes or []
        self.q1 = self.q2 = self.q3 = Queue()


def main():
    from process import Process
    from rawdata import RawData
    data = RawData()
    processes = data.processes()
    for i, p in enumerate(processes):
        proc = Process(i+1, p)
        print('P{number}'.format(number=proc.number))
        print('CPU len: {len}'.format(len=len(proc.schedule['cpu'])))
        print('IO len: {len}'.format(len=len(proc.schedule['io'])))
        print('===================')

if __name__ == '__main__':
    main()
