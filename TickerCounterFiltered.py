import csv
from TickerCounter import TickerCounter


class TickerCounterFiltered(TickerCounter):
    banned_tickers = []
    def __init__(self):
        with open('banned_tickers.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                self.banned_tickers.append(row[0])
        super().__init__()


    def is_ticker_usable(self, ticker):
        if(ticker in self.banned_tickers):
            print('false')
            return False
        return super().is_ticker_usable(ticker)
