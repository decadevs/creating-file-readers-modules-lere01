from .interface import ModuleInterface

class TextFile(ModuleInterface):
    def __init__(self, filename, mode='r'):
        self.filename = filename

    def read_all_lines(self):
        with open(self.filename) as fd:
            return list((line.rstrip() for line in fd))

    def read_first_two_lines(self):
        with open(self.filename) as fd:
            return list((line.rstrip() for line in fd))[:2]


    def read_last_two_lines(self):
        with open(self.filename) as fd:
            return list((line.rstrip() for line in fd))[-2:]



    