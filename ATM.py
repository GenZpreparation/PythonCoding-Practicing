Balance=2000
User_pin=1234

print("Wellcome Pentagon ATM")
card=int(input("Insert the Card : "))


if card==1:
    language=input("Select Language : English, Hindi : ")
    pin=int(input("Enter your Pin : "))
    if pin!=User_pin:
        print("Your Pin is Wrong")
    else:
        task=input("Select Check Balance, Withdraw : ")
        if task=="Balance":
            print(f"Your Balance is {Balance} ")
        else:
            depo=int(input("Enter amount : "))
            if depo<= Balance and depo>=100 and depo%100==0:
                Balance -= depo
                print("Amount Withdraw Successful")
                print("ThankU , Visit again")
            else:
                print("Enter valid amount")
else:
    print("Please Insert your card Correctly" )






