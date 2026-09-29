class Villain:
    def __init__(self):
        self.name="Rukku"
        self.age=28

    def act(self):
        print("Rukku is Pretty Actress")
# --------------------------------------
v1=Villain()
print(v1.name)
print(v1.age)
v1.act()
v1.movies="Toxic"
print(v1.movies)
v1.age=30
print(v1.age)
del v1.age
print(v1.age)
