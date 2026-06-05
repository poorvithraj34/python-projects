# a=int(input("enter the value of a"))
# b=int(input("enter the value of b"))
# print("choose a opeartor")
# print("1-add")
# print("2-substact")
# print("3-multiply")
# print("4-divide")
# choice=int(input("enter the choice"))
# if choice==1:
#     print("result",a+b)
# elif choice==2:
#     print("result",a-b)
# elif choice==3:
#     print("result",a*b)
# elif choice==4:
#     if b!=0:
#         print("result",a/b)
#     else:
#         print("cannnot divide by zero")
# else:
#     print("invalid opeartion")




# name=input("enter the name")
# birth_year=int(input("enter the birth year"))
# current_year=2026
# age=current_year-birth_year
# if age>=60:
#     print("senior citizen",name)
# else:
#     print("not a senior citizen",name)




# n=int(input("enter the value of n"))
# a=0
# b=1
# count=0
# if count<=n:
#     print("fibonacci series")
#     for i in range(n):
#         print(a,end="")
#         a,b=b,a+b




lis=[]
while True:
    print("\n list operation menu")
    print("1.inset element")
    print("2.remove element")
    print("3.append element")
    print("4.dispaly length")
    print("5.pop an elemnt")
    print("6.clear list")
    print("7.exit")

    choice=int(input("enter the choice"))
    if choice==1:
        element=int(input("enter element to insert"))
        position=int(input("enetr the position"))
        lis.insert(element,position)

    elif choice==2:
        element=int(input("enter the element to remove"))
        if element in lis:
            lis.remove(element)
        else:
            print("element not found")


    elif choice==3:
        element=int(input("enter the element to append"))
        lis.append(element)

    elif choice==4:
        print("length of list",len(lis))

    elif choice==5:
        if lis:
            lis.pop()
        else:
            print("list is empty")
    
    
    elif choice==6:
        lis.clear()
        print("list cleared")

    elif choice==7:
        break

    else:
        print("invalid choice")           



# import math
# n=int(input("enter the value of n"))
# numbers=[]
# for i in range(n):
#     value=float(input(f"enter element {i+1}:"))
#     numbers.append(value)
# mean=sum(numbers)/n

# total=0
# for x in numbers:
#     total=total+(mean-x)**2
# variance=total/n

# std_dev=math.sqrt(variance)


# print(mean,"mean")
# print(variance,"variamce")
# print(std_dev,"std_dev")


# #frequency of each digit

# from math import sqrt
# num=input("enter the number")
# uniq_dig=set(num)
# for elem in uniq_dig:
#     print(elem,"occours",num.count(elem),"times")




# def divExp(a,b):
#     if a>b:
#         raise Exception("a is greater than b")
#     if b==0:
#         raise ZeroDivisionError("division by zero")
#     return a/b

# try:
#     a=float(input("enter the value of a"))
#     b=float(input("enter the value of b"))
#     result=divExp(a,b)
#     print("result",result)

# except ZeroDivisionError as z:

#  print("zerodivisionerror",z)
# except ValueError:
#  print("enter number only")
# except Exception as e:
#  print("expection,e")



# with open("input.txt","r") as infile:
#     lines=infile.readlines()
# data=[line.strip() for line in lines]
# data.sort()

# with open("output.txt","w") as outfile:
#     for item in data:
#         outfile.write(item+"\n")
# print("sorted succssfully")
# print("sorted content are written to output.txt")



# def DivExp(a,b):
#     if a>b:
#         raise Exception("a is greater than b")
#     if b==0:
#         raise ZeroDivisionError("division by zero is not allowed")
#     return a/b
    
# try:
#     a=float(input("enter the value of a"))
#     b=float(input("enter the value of b"))
#     result=DivExp(a,b)
#     print("result",result)

# except ZeroDivisionError as z:
#     print("zerodivisionerror,",z)
# except ValueError:
#     print("enter numbers only")
# except Exception as e:
#     print("expection",e)            




# with open("infile.txt","r") as infile:
#     lines=infile.readlines()
#     data=[line.strip() for line in lines]
#     data.sort()

# with open("outfile.txt","w") as outfile:
#     for item in data:
#         outfile.write(item+"\n")

# print("data sorted succesfully")
# print("sorted content is equal to output.txt")        




# def divexp(a,b):
#     assert a>0, "a must be greater than 0"
#     if b==0:
#         raise ZeroDivisionError("division by zero is not allowed")
#     return a/b

# try:
#     a=float(input("enter the value of a"))
#     b=float(input("enter the value of b"))
#     result=divexp(a,b)
#     print("result",result)
# except AssertionError as ae:
#     print("assertionerror",a)
# except ValueError :
#     print("put numbers only")
# except ZeroDivisionError as z:
#     print("zero",z) 
# 
# 
# 
# with open ("input.txt","r") as infile:
#     lines=infile.readlines()
#     data=[line.strip() for line in lines]
#     data.sort()

# with open("output.txt","w") as outfile:
#     for item in data:
#         outfile.write(item+"\n")


# from math import sqrt
# num=input("enter the value of n")
# uniq_dig=set(num)
# for elem in uniq_dig:
#     print(elem,"occours",num.count(elem),"times")




# import math
# n=int(input("enter the value of n"))
# numbers=[]
# for i in range(n):
#     value=float(input(f"element no {i+1}"))
#     numbers.append(value)

# mean=sum(numbers)/n

# total=0
# for x in numbers:
#     total=total+(x-mean)**2
# var=total/n

# dev=math.sqrt(var)

# print(mean,var,dev)
