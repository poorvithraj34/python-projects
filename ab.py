tup=(6,7,3,4,1,5)
lis=list(tup)
for i in range(len(lis)):
    for j in range(len(lis)-1):
        if lis[j]>lis[j+1]:
            temp=lis[j]
            lis[j]=lis[j+1]
            lis[j+1]=temp
sorted_tuple=tuple(lis)
print(sorted_tuple)           




           