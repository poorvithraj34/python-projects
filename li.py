employees = {
    101: ("Ram", "HR", 50000),
    102: ("Sam", "Manager", 70000),
    103: ("Riya", "Developer", 65000)
}
highest=0
top_employee=""
for eid,data in employees.items():
    salary=data[2]
    if salary>highest:
        highest=salary
        top_employee=data[0]
print(highest)
print(top_employee)        

        

    