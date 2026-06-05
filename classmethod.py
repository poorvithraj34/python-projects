class computer:
    brand="mercedes"
    def __init__(self,ram,cpu):
        self.ram=ram
        self.cpu=cpu

    @classmethod #it is used to access a class its used
    def info(cls):
        return cls.brand
    
    @classmethod
    def change_name(cls,brand):
        cls.brand=brand
        
    
    @staticmethod#it depends on nothing to do any independent function we use it
    def gb_to_bytes(gb):
        return gb*3
    


c1=computer(30,50)
print(c1.ram)
print(c1.cpu)
print(computer.info())    
print(c1.gb_to_bytes(9))
c1.change_name=("poorvith")
print(c1.change_name)