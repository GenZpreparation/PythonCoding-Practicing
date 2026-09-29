

class info:
    def __init__(self,name,age,salary=10000):
        self.name=name
        self.age=age
        self.salary=salary
    def __str__(self):
        return f"{self.name} , {self.age} , {self.salary}"


p1=info("Abhi",22)

p2=info("Ankush",21,25000)

print(f"{p1.name}, {p1.age},{p1.salary}")


print(p2)


