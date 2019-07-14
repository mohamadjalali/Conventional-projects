from bank import SavingsAccount

class RestricatedSavingsAccount(SavingsAccount):
    """This class represents a restricated savings account."""

    MAX_WITHDRAWALS = 3

    def __init__(self, name, pin, balance = 0.0):
        """Same attributes as SavingSAccount, but with
        a counter for withdrawals."""
        SavingsAccount.__init__(self, name, pin, balance)
        self._counter = 0

    def withdraw(self, amount):
        """Restricts number of withdrawals to MAX_WITHDRAWALS."""
        if self._counter == RestricatedSavingsAccount.MAX_WITHDRAWALS:
            return "No more withdrawals this month"
        else:
            message = SavingsAccount.withdraw(self, amount)
            if message == None:
                self._counter += 1
            return message

    def resetCounter(self):
        self._counter = 0


account = RestricatedSavingsAccount("Ken", "1001", 500.00)
print(account)
print("---------------------------------")
for count in range(3):
    account.withdraw(100)
print(account.getBalance())
account.resetCounter()
print(account.withdraw(50))
# print(account.getBalance())
