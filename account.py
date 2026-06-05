class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        


    def debit(self , amount):
        self.balance-=amount
        print("rs",amount,"debited from your account")
        print("total balance is",self.get_balance())


    def credit(self, amount):
        self.balance += amount
        print("rs",amount,"credited into your account")
        print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance


acc1=Account(1250,123456)
acc1.credit(300)
acc1.debit(1000)
