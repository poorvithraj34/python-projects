n1=[]
n2=[]
s=[]
for i in range(3):
    row=[]
    for j in range(3):
        val=int(input("enter:"))
        row.append(val)
    n1.append(row)
for i in range(3):
    row=[]
    for j in range(3):
        val=int(input("enter:"))
        row.append(val)
    n2.append(row)
for i in range(3):
    row=[]
    for j in range(3):
        sa=n1[i][j]+n2[i][j]
        row.append(sa)
    s.append(row)
for i in range(3):
    print(s[i])