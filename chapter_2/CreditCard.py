class CreditCard:
    """ A consumer card. """
    def __init__(self, customer, bank, acnt, limit):
        """ Create a new credit card instance

        The initial balance is zero

        customer the name of the customer (e.g "Eduard B")
        bank     the name of the bank (e.g Metro Bank)
        acnt     the account identifier (e.g 9422 2223 4444 22232)
        limit     credit limit (measured in £)
        """

        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """ Return the name of the customer """
        return self._customer
    
    def get_bank(self):
        """ Return the banks name"""
        return self._bank
    
    def get_account(self):
        """ Return the card identifier """
        return self._acnt
    
    def get_limit(self):
        """ Return the current credit limit """
        return self._limit
    
    def get_balance(self):
        """Return current balance"""
        return self._balance

    def charge(self, price):
        """ Charge given price to the card, assuming sufficient credit limit
        Return True if charge was processed otherwise False """

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """ Process customer payment that reduces balance"""
        self._balance -= amount


jack = CreditCard('Jackson', 'Deutsche', '3222 2222 4444 3333', 200000)

print(vars(jack))