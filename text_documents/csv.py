import csv
from .interface import ModuleInterface

class CSVFile(ModuleInterface):
    def __init__(self, filename, mode='r'):
        self.filename = filename

    def read_all_lines(self):
        with open(self.filename) as fd:
            csvreader = csv.reader(fd)
            return list((line for line in csvreader))

    def read_first_two_lines(self):
        with open(self.filename) as fd:
            csvreader = csv.reader(fd)
            return list((line for line in csvreader))[:2]


    def read_last_two_lines(self):
        with open(self.filename) as fd:
            csvreader = csv.reader(fd)
            return list((line for line in csvreader))[-2:]



    