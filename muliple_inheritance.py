class A:
    var1="welocome"


class B:
    var2="to"


class C(A,B):
    var3="our universe"



c1=C()
print(c1.var1)
print(c1.var2)
print(c1.var3)