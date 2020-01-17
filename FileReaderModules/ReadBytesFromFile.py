from ModuleInterface.interface import ModuleInterface


class OpenFIle:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_trace_back):
        self.file.close()




class ReadFile(ModuleInterface):
    def __init__(self, file_descriptor):
        self.file_desc = file_descriptor
        self.lines = []


    def read_all_lines(self):
        self.lines = list((line.rstrip() for line in self.file_desc))
        return self.lines


    def read_first_two_lines(self):
        return list((line.rstrip() for line in self.file_desc))[:2]


    def read_last_two_lines(self):
        return list((line.rstrip() for line in self.file_desc))[-2:]



    
class FileIterator:
    def __init__(self, file_descriptor):
        self.opened_file = file_descriptor

    def __iter__(self):
        return self

    def __next__(self):
        for line in self.opened_file:
            return line