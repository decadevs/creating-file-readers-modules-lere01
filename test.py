import unittest
from text_documents.text import TextFile
from text_documents.csv import CSVFile
from text_documents.tsv import TSVFile
from spreadsheets.csv import CSVSpread
from spreadsheets.tsv import TSVSpread


class TestClass(unittest.TestCase):    
    def test_OpenTextFile(self):
        text_file = TextFile('numbers.txt')
        self.assertListEqual(text_file.read_first_two_lines(), ['1', '3'])
        self.assertListEqual(text_file.read_last_two_lines(), ['44', '31'])
        self.assertListEqual(text_file.read_all_lines(), ['1', '3', '99', '100', '120', '32', '330', '23', '76', '44', '31'])
    
    
    def test_OpenCSVFile(self):
        csv_file = CSVFile('techcrunch.csv')
        self.assertListEqual(csv_file.read_first_two_lines(), [['permalink', 'company', 'numEmps', 'category', 'city', 'state', 'fundedDate', 'raisedAmt', 'raisedCurrency', 'round'], 
['lifelock', 'LifeLock', '', 'web', 'Tempe', 'AZ', '1-May-07', '6850000', 'USD', 'b']])
        self.assertListEqual(csv_file.read_last_two_lines(), [['grid-networks', 'Grid Networks', '', 'web', 'Seattle', 'WA', '30-Oct-07', '9500000', 'USD', 'a'], ['grid-networks', 'Grid Networks', '', 'web', 'Seattle', 'WA', '20-May-08', '10500000', 'USD', 'b']])
    
    
    def test_OpenTSVFile(self):
        tsv_file = TSVFile('random.tsv')
        self.assertListEqual(tsv_file.read_first_two_lines(), [['ï»¿driving', 'birthday', 'education', 'play', 'tool', 'plane', 'handle', 'dollar'], ['solid', 'whatever', 'able', 'earth', 'dry', 'specific', 'do', 'take']])
        self.assertListEqual(tsv_file.read_last_two_lines(), [['missing', 'running', 'complete', 'card', 'happily', 'rhyme', 'main', 'same'], ['balloon', 'production', 'tax', 'hardly', 'air', 'mirror', 'satellites', 'floor']])


if __name__ == '__main__':
    unittest.main()
