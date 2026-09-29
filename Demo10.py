class Laptop:
    def __init__(my):
        my.brand="HP"
        my.color="Black"
        my.cost=570000
    def on(my):
        print("LapTop is on")
        my.storage=128
    def off(my):
        print("Laptop is off")

l1=Laptop()
print(l1.brand)
print(l1.cost)
print(l1.color)

l1.on()
l1.off()
print(l1.storage)


