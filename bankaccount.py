class BankAccount:
    def __init__(self,name,pin,balance=0):
        self.name=name
        self.pin=pin

        self.balance=balance

        self.history=[]


    def deposit(self,amount):

        self.balance+=amount

        self.history.append(f"deposit ${amount}")
        print(f"${amount} deposited ! new balance: ${self.balance}")


    def withdraw(self,amount):

        if amount <= self.balance:

            self.balance-=amount


            self.history.append(f"withdraw  ${amount}")
            print(f"${amount} withdraw ! new balance : ${self.balance}")

        else:
            print("insufficient funds")

    def show_balance(self):
        print(f"Account holder {self.name},Account balance ${self.balance}")



    def show_history(self):

        print("\n --- Transction history---")

        for t in self.history:

            print(t) if self.history else print("no transaction yet!")



name=input("Enter your name ")
pin=input("enter your pin")
account=BankAccount(name,pin)

if input("enter pin to login")!= account.pin:
    print("wrong pin! access denied.")

    exit()

while True:

    print("\n1.deposit  2.withdrwa 3.show balance 4.history 5.exit")
    
    choice=input("choose:")

    if choice=="1":

        account.deposit(int(input("enter the amount")))
    
    elif choice =="2":

        account.withdraw(int(input("enter the amount")))

    elif choice =="3":

        account.show_balance()


    elif choice =="4":

        account.show_history()


    elif choice =="5":

        print("goodbye!")


        break

    else:

        print("invalid choice")











    
            


    

       

