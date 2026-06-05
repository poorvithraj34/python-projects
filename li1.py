d = {
    "a": 5,
    "b": 2,
    "c": 8
}
lis=list(d.items())
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i][1]>lis[j][1]:
            temp=lis[i]
            lis[i]=lis[j]
            lis[j]=temp
sorted_lis=dict(lis)
print(sorted_lis)            


