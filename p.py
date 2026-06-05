nums=[2,7,9,8,4]
target=9
dict={}
for i in range(len(nums)):
    complement=target-nums[i]
    if complement in dict:
        print(dict[complement],i)

    dict[nums[i]]=i