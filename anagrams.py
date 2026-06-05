s1="listen"
s2="silent"
dict1={}
dict2={}
for ch in s1:
    if ch in dict1:
        dict1[ch]+=1
    else:
        dict1[ch]=1

for ch in s2:
    if ch in dict2:
        
        dict2[ch]+=1
    else:
        dict2[ch]=1


print(dict1==dict2)
