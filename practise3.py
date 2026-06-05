with open("practise.txt","r") as f:
    data=f.read()
    data_1=data.replace("poorvith","samarth")
    print(data_1)

with open("practise.txt","w") as f:
    f.write(data)

