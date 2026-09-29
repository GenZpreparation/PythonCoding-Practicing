class Hero:
    def __init__(self):
        self.name="DBOSS"
        self.age=49
        self.numberOfMovies=56
    def act(self):
        print("Dboss is best actor")

h1=Hero()
print(h1.name)
print(h1.age)
print(h1.numberOfMovies)
h1.act()


class Fan:
    def __init__(self):
        self.brand="USHA"
        self.color="Black"
        self.wings=3
        self.cost=2000
    def on(self):
        print("Fan is ON")
    def off(self):
        print("Fan is OFF")
    def rotate(self):
        print("Fan is rotating")


f1=Fan()
print(f1.brand)
print(f1.cost)
print(f1.color)
print(f1.wings)
f1.on()
f1.off()
f1.rotate()

