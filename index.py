def print_list(list,idx=0):
    if(idx==len(list)):
        return 0
    
    print_list(list, idx+1 )
    print(list[idx])

names=["poorvith","kioshore","bhuvan"]

print_list(names)