m1=int(input("enter marks 1"))
m2=int(input("enter marks 2"))
m3=int(input("enter marks 3"))
m4=int(input("enter marks 4"))
average=(m1+m2+m3+m4)/4
if average>=75:
    print("grade is distinction")
elif average>=60 and average<75:
    print("grade is first division")
elif average>=50 and average<60:
    print("grade is second division")
elif average>=40 and average<50:
    print("grade is third division")
else:
    print("fail")
