class Stock:
    def __init__(self, ticker, open, close, volume):
        self.ticker = ticker
        self.open = open
        self.close = close
        self.volume = volume
        self.rate_return = float(close) / open - 1

    def update(self, open, close):
        self.open = open
        self.close = close
        self.rate_return = float(self.close) / self.open - 1

    def print_return(self):
        print (self.rate_return)

class child(Stock):
    def __init__(self, name):
        self.name = name

def main():
    aa = child('AA')
    print (aa.name)
    aa.update(100, 102)
    print (aa.open)
    print (aa.close)
    print (aa.rate_return)
    apple = Stock('AAPL', 143.69, 144.09, 20109375)
    google = Stock('GOOGL', 898.7, 911.7, 1561616)
    print (apple.ticker)
    apple.print_return()
    apple.ceo = 'Tim cook'
    print (apple.ceo)
    print (dir(apple))
    print (google.ticker)
    google.print_return()
    google.update(912.8, 913.4)
    google.print_return()


if __name__ == '__main__':
    main()


