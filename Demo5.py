class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def desplay(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")

    def is_pass(self):
        if self.marks>40:
            print("Pass")
        else:
            print("Fail")

st1=Student("Abhi",23,38)

st1.desplay()
st1.is_pass()

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        print(f"Area: {self.length*self.width}")

    def parameter(self):
        print(f"Parameter: {2*(self.length+self.width)}")
        

r1=Rectangle(12,24)
r1.area()
r1.parameter()


class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print(f"")


        