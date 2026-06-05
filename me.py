nums=[2,2,2,4,5,2,2]
dict={}
for num in nums:
    if num in dict:
        dict[num]+=1
    else:
        dict[num]=1
         
for key,value in dict.items():
    if value>len(nums)//2:
        print(key)       