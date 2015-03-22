__author__ = 'matthewburleson'

class Store:
    open = 9
    close = 6

    def hours(self):
        print("We're open from {open} to {close}.".format(open=self.open, close=self.close))

seven_eleven = Store()
seven_eleven.hours()