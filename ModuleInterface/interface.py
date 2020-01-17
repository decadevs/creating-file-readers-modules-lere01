from abc import ABC, abstractmethod

class ModuleInterface(ABC):
    @abstractmethod
    def read_all_lines(self):
        pass

    @abstractmethod
    def read_first_two_lines(self, num_of_lines=2):
        pass

    @abstractmethod
    def read_last_two_lines(self):
        pass









