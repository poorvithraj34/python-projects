class grandfather():
    def __init__(self,name):
        self.name=name

class father(grandfather):
    def __init__(self,name):
        super().__init__(name)

class son(father):
    def __init__(self,name):
        super().__init__(name)

s1=son("poorvith")
print(s1.name)                        



