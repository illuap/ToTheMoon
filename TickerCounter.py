import csv

class TickerCounter(object):

    counter: dict = None

    def __init__(self):
        self.counter = dict()

        self.get_tickers_from_csv('amex')
        self.get_tickers_from_csv('nasdaq')
        self.get_tickers_from_csv('nyse')
        #print (self.counter)

    def is_ticker_usable(self, ticker):
        return True

    def get_file_path(self, filename):
        return "Tickers/"+filename+'.csv'

    def get_csv_dictreader(self, file):
        return csv.DictReader(file, delimiter=',', quotechar='|')

    def get_tickers_from_csv(self, filename):
        with open(self.get_file_path(filename), newline='') as csvfile:
            spamreader = self.get_csv_dictreader(csvfile) 
            for row in spamreader:
                symbol = row['Symbol']
                if self.is_ticker_usable(symbol):
                    self.counter[row['Symbol']] = 0

    def get_ticker_count(self) -> dict:
        new_counter = dict()

        for key in self.counter.keys():
            if self.counter[key] > 0:
                new_counter[key] = self.counter[key]

        sorted_counter = {k: v for k, v in sorted(new_counter.items(), key=lambda item: item[1], reverse=True)}
        return sorted_counter