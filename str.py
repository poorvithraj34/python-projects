words=["tea","ate","eat","tta","ale"]
dict={}
for word in words:
    key="".join(sorted(word))
    if key in dict:
        dict[key].append(word)
    else:
        dict[key]=[word]
print(list(dict.values()))        
    
              
