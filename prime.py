num=int(input("enter the value of number"))
if num<=1:
   print("not a prime number")
else:
   for i in range(2,num):
    if num%i==0:
      print("not a prime number")
   else:
      print("prime number")