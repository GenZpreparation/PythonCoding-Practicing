# class Farmar:
#     def __init__(self,p,t,r):
#         self.principle=p
#         self.time=t
#         self.rate=r
#
#     def Loan(self):
#         si=(self.principle*self.time*self.rate)/100
#         print(si)
#
# f1=Farmar(200000,3,2.5)
# f2=Farmar(300000,4,2.5)
# f1.Loan()
# f2.Loan()
#


class Farmar:
    r=2.5
    def __init__(self,p,t):
        self.principle=p
        self.time=t


    def Loan(self):
        si=(self.principle*self.time*Farmar.r)/100
        print(si)

f1=Farmar(200000,3)
f2=Farmar(300000,4)
f1.Loan()
f2.Loan()

