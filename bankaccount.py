class BankAccount:
    def __init__(self, int_rate, balance):
        self.int = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self

    def withdraw(self, amount):
        self.balance -= amount
        print(self.balance)
        return self

    def display_account_balance(self):
        print(self.balance,self.int)
        return self

    def yield_interest(self):
        if (self.balance>0):
            self.int = self.int*1.5
        else:
            pass
        return self

# acc_1 = BankAccount(11,5000)
# acc_2 = BankAccount(1,300)

# acc_1.deposit(40).deposit(100).deposit(20).withdraw(100).yield_interest().display_account_balance()
# acc_2.deposit(200).deposit(300).withdraw(50).withdraw(30).withdraw(100).withdraw(70).yield_interest().display_account_balance()