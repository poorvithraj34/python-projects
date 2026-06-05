var="good"
def show():
    global var
    var="morning"
    print("in function",var)

show()
print("outside function",var)
var="perfect"
print("upadted function",var)    
