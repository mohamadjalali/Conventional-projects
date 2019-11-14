import _pickle as cPickle

class SavingsAccount(object):
    """This class represents a Saving account
    with the owner's name, PIN, and balance."""

    RATE = 0.02

    def __init__(self, name, pin, balance = 0.0):
        self._name    = name
        self._pin     = pin
        self._balance = balance

    def __str__(self):
        result  = 'Name:     ' + self._name + '\n'
        result += 'PIN:      ' + self._pin  + '\n'
        result += 'Balance:  ' + str(self._balance)
        return result

    def getBalance(self):
        return self._balance

    def getName(self):
        return self._name

    def getPin(self):
        return self._pin

    def deposit(self, amount):
        """Deposit the given amount and returns the
        new balance."""
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        """Withdraws the given amount.
        Return None if successful, or an
        error message if unsuccessful."""
        if amount < 0:
            return 'Amount must be >= 0'
        elif self._balance < amount:
            return 'Insufficient funds'
        else:
            self._balance -= amount
            return None

    def computeInterest(self):
        """Computes, deposit, and return the interest."""
        interest = self._balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest


class Bank(object):
    def __init__(self, fileName = None):
        self._accounts = {}
        self._fileName = fileName
        if fileName != None:
            fileObj  = open(fileName, 'rb')
            while True:
                try:
                    account = cPickle.load(fileObj)
                    print (account)
                except EOFError:
                    fileObj.close()
                    break
    
    def __str__(self):
        """Return the string rep of the entire bank."""
        return '\n'.join(map(str, self._accounts.values()))

    def add(self, account):
        """Inserts and account using its PIN as a key."""
        self._accounts[account.getPin()] = account

    def remove(self, pin):
        return self._accounts.pop(pin, None)

    def get(self, pin):
        return self._accounts.get(pin, None)
        return self._accounts.values()
    
    def computeInterest(self):
        """Compute interest for each account and
        returns the total."""
        total = 0.0
        for account in self._accounts.values():
            total += account.computeInterest()
        return total
    
    def save(self, fileName = None):
        """Saves pockled accounts to a file.  The parameter
        allows the user to change filename."""
        if fileName != None:
            self._fileName = fileName
        elif self._fileName == None:
            return 
        fileObj = open(self._fileName, 'wb')
        for account in self._accounts.values():
            cPickle.dump(account, fileObj)
        fileObj.close()
        print("successful saved")

# bank  = Bank()
# bank.add(SavingsAccount("arian", "1001", 4000.00))
# bank.save('bank.dat')
# bank.__init__('bank.dat')
