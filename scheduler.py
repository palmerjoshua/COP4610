from process import Process
from rawdata import RawData

class Scheduler:
    def __init__(self, processes=None):
        self.processes = processes or []
        pass


def main():
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
