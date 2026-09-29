import time
password=1234
Balance=10000
print("Welcome to Pentagon ATM")
print("Insert your card")
print("Press 1.Yes 2.No")
choice=int(input())
if choice==1:
    print("Select your language")
    print("Press 1.English 2.Kannada 3.Telugu")
    lang=int(input())
    if lang==1:
        print("Enter your pin")
        pin=int(input())
        if pin==password:
            print("select the options")
            print("Press 1.Bal enq 2.withdrawl")
            choice1=int(input())
            if choice1==1:
                print("your available balance is",Balance)
            elif choice1==2:
                print("Enter the amount")
                amt=int(input())
                if amt<=Balance and amt%100==0:
                    print("your Transaction is proccessing")
                    time.sleep(5)
                    print("please wait")
                    time.sleep(3)
                    print("collect your cash")
                    time.sleep(4)
                    print("do you want to check your balance")
                    print("Press 1.yes 2.No")
                    choice2 = int(input())
                    if choice2 == 1:
                        print("your available balance is", Balance - amt)
                        print("thank you visit again")
                    else:
                        print("Thank you visit again")
                else:
                    print("Enter Valid amount")
            else:
                print("select the correct option")
        else:
            print("invalid pin")
    else:
        print("please select english")
else:
    print("insert your card properly")


