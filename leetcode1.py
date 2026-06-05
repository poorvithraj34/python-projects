#nums=[1,3,5,2,2]
#ound=False
#for i in range(len(nums)):
   # for j in range(i+1,len(nums)):
       # if nums[i]+nums[j]==target:
          #  found=True
           # break
        

#if found:
   # print(True)
#else:
    #print(False)
    # 


#def two_numbers(nums,target):
 #   seen={}
 #   for i in range(len(nums)):
 #       diff=target-nums[i]
  #      if diff in seen:
  #          return [seen[diff],i]
        
   #     seen[nums[i]]=i


#print(two_numbers([3,2,4],6))  
nums=[2,3,3,3,4,5,6,6]
duplicate=[]
seen=[]
for i in nums:
    if i in seen:
        if i not in duplicate:
            duplicate.append(i)


    else:
        seen.append(i)


print(duplicate)

       

       



                 


    
