def calc_sum(n):
    if(n==0):
        return 1
    else:
        return calc_sum(n-1)+n
sum=calc_sum(5)
print(sum)





    

    