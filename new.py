def outer():
    print("Inside Outer")
    def inner():
        print("Inside Inner")
    inner()
    

outer()



