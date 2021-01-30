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


print(__name__)
if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard( 'John Bowman' , 'California Savings' ,
    '5391 0375 9387 5309' , 2500) )
    wallet.append(CreditCard( 'John Bowman' , 'California Federal' ,
    '3485 0399 3395 1954' , 3500) )
    wallet.append(CreditCard( 'John Bowman' , 'California Finance' ,
    '5391 0375 9387 5309', 5000))
    

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)
    
    for c in range(3):
        print('Customer=', wallet[c].get_customer())
        print('Bank=', wallet[c].get_bank())
        print('Account=', wallet[c].get_account())
        print('Limit=', wallet[c].get_limit())
        print('Balance=', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance = ', wallet[c].get_balance())
        print()

class PredatoryCreditCard(CreditCard):
    OVERLIMIT_FEE = 5

    """ An extension to CreditCard that compounds interest and fees """
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += PredatoryCreditCard.OVERLIMIT_FEE
        return success
    
    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor

