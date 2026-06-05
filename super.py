class student:
    def __init__(self,name):
        self.name=name
        print("constructor of student")

class person(student):
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
        print("constructor")


c1=person("poorvith",18)
print(c1.name)
print(c1.age)



#another example
class animal:
    def __init__(self,speak):
        self.speak=speak
        print("animals make sound")




class dog(animal):
    def __init__(self,speak):
        super().__init__(speak)
        print("dog barks")


a1=dog("barks")
print(a1.speak)            