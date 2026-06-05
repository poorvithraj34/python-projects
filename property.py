class student:
    def __init__(self,phy,che,bio):
        self.phy=phy
        self.che=che
        self.bio=bio


    @property
    def percentage(self):
        return str((self.phy+self.che+self.bio)/3)+"%"


s1=student(90,95,87)
print(s1.percentage)

s1.phy=87
print(s1.percentage)