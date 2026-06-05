class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    @staticmethod
    def hello():
        print("hello")
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        avg=sum/len(self.marks)
        print( "hi",self.name,"your average marks is",avg)


s1=student("poorvith",[2,6,7])
s1.get_avg()
s1.hello()       