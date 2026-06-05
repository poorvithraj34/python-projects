nums=[2,3,4,3,3,4,5]
count= {}

for i in nums:
    if i in count:
        count[i]+=1
    else:
        count[i]=1


for i in nums:
    if count[i]==1:
        print(i)

    

