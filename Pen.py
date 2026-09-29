class Pen:
    def __init__(self):
        self.color="Red"
        self.brand="Reynolds"
    def write(self):
        print("Pen is writing")
        print(self.color)
        print(self)

p1=Pen()
print(p1.color)
print(p1.brand)
p1.write()
print(p1)

p2=Pen()
print(p2)
p2.write()
