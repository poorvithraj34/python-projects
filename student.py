class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary



    def show_details(self):
        print("role",self.role)
        print("dept",self.dept)
        print("salary",self.salary)


class engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age 
        super().__init__("engineering","IT",75000)        



c1=engineer("poorvith",18)
c1.show_details()
print(c1.name,c1.age)



class order:
    def __init__(self,item,value):
        self.item=item
        self.value=value


    def __gt__(self,odr2):
        return self.value > odr2.value



c1=order("tea",25)
c2=order("chips",30)

print(c1>c2)
print(c1<c2)


    