n=int(input("enter the value of n"))
print("collatz sequence")
steps=0
while n!=1:
    print(n,end=" ")


    if n%2==0:
        n=n//2
    else:
        n=3*n+1

    steps=steps+1

print(1)
print("total steps",steps)
