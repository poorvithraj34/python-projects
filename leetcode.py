nums=[2,6,5,3,7]
target=5
flag= False
for i in range(len(nums)):
    for j in range (i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(i,j)
            flag=True
            break


    if flag:
        break


