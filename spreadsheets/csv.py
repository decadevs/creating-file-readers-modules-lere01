import pandas as pd
from text_documents.interface import ModuleInterface

class CSVSpread:
    def __init__(self, filename):
        self.filename = filename

    def read_all_lines(self):
        return pd.read_csv(self.filename)

    def read_first_two_lines(self):
        return pd.read_csv(self.filename).head(2)


    def read_last_two_lines(self):
        return pd.read_csv(self.filename).tail(2)