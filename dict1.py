nums=[1,2,3,4,5]
dict={}
count=0
for i in nums:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)

