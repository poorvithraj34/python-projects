count=1
with open("poorvith.txt","r") as f:
    data=f.read()

    nums=""
    result=[]
    for ch in data:
        if ch==",":
            result.append(nums)
            nums=""
        else:
            nums+=ch


print(result)