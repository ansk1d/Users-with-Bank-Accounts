from bankaccount import BankAccount


class User:
    def __init__(self,name):
        self.name = name

    def make_deposit(self,amount):
        self.deposit += amount
        print(self.balance)
        return self

    def make_withdrawal(self, amount):
        if (self.withdraw < amount):
            print(f"Sorry {self.name}!\n You don't have enough Money")
        else:
            self.withdraw -= amount
            print(self.withdraw)
        return self
        

    def display_user_balance(self):
        print(self.name,self.balance)
        return self


    def transfer_money(self,otheruser,amount):
        if(amount>self.balance):
            print(f"Sorry {self.name}! You don't have enough Money")
        else:
            self.balance -= amount
            otheruser.balance += amount
            return self



first_user = User("faisal",5000)
sec_user = User("anas",4000)
third_user = User("ali",3000)

# first_user.display_user_balance().make_deposit(400).display_user_balance().make_deposit(400).make_deposit(400).display_user_balance()
# sec_user.make_deposit(100).make_withdrawal(500).display_user_balance().make_deposit(200).make_withdrawal(100).display_user_balance()
# third_user.make_deposit(1000).make_withdrawal(200).make_withdrawal(250).make_withdrawal(300).display_user_balance()
first_user.transfer_money(third_user,2000).display_user_balance()
third_user.display_user_balance()

