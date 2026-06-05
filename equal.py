def check_relation(a,b):
    if(a==b):
        return 0
    if(a>b):
        return 1
    if(a<b):
        return -1

a=4
b=5
check_relation(a,b)
if(a==b):
    print("a is equal to b")
if(a>b):
    print("a is greater than b")
if(a<b):
    print("a is less than b")    

