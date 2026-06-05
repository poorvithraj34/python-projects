class car:

    @staticmethod
    def start():
        print("car started")


    @staticmethod
    def stop():
        print("car stopped")


class toyatacar(car):
    def __init__(self,name):
        self.name=name



class fortunur(toyatacar):
    def __init__(self,type):
        self.type=type


s1=fortunur("petrol")
s1=toyatacar("poorvith")
print(s1.name)                

