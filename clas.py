class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc

    def debit(self,amount):
        self.balance-=amount
        print("rs",amount,"was debited")
        print("total balanace",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("rs",amount,"was credited")
        print("total balanace",self.get_balance())

    def get_balance(self):
        return self.balance    

    

acc1=account(10000,12345)
acc1.debit(200)
acc1.credit (100)             