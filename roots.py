import math
a=float(input("enter the value of a"))
b=float(input("enter the value of b"))
c=float(input("enter the value of c"))
d=b*b-4*a*c

if d>0:
    r1=(-b+math.sqrt(d)/(2*a))
    r2=(-b-math.sqrt(d)/(2*a))
    print("roots are real and distinct")
    print("root1=",r1)
    print("root2=",r2)
     
elif d<0:
    r=-b/(2*a)
    print("roots are real and equal")
    print("root",r)

else:
    real=-b/(2*a)
    imag= math.sqrt(-d)/(2*a)
    print("roots are imaginary")
    print("root 1=",real, "+",imag,"i")
    print("root2=",real,"-",imag,"i")



