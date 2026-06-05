class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag


    def shownumber(self):
        print(self.real,"i+",self.imag,"j")


    def __add__(self,num2):#this is a dunder function
        newreal=self.real+num2.real
        newimag=self.imag+num2.imag
        return complex(newreal,newimag)
    

    def __sub__(self,num2):#this is a dunder function
        newreal=self.real-num2.real
        newimag=self.imag-num2.imag
        return complex(newreal,newimag)



c1=complex(4,6)
c1.shownumber()

c2=complex(3,5)
c2.shownumber()


c3=c1+c2
c3.shownumber()

c3=c1-c2
c3.shownumber()

