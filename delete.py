class Account:
    def __init__(self,acc_num,acc_pass):
        self.acc_num=acc_num
        self.__acc_pass=acc_pass

    def reset_password(self):
        print(self.__acc_pass)    


c1=Account(12345,"poorvith123")
print(c1.reset_password())
