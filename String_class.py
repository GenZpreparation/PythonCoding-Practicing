# str="Abhi"
# print(str)
# print(str[0])
# print(str[1])
# print(str[-1])
# print(str[-2])

# Slicing _____________------------------------------------ _________________
# str="RajaRamMohanRoy"
# print(str[2:8])
# print(str[1:6])
# print(str[2:8:2])
# print(str[-2:-8])
# print(str[-2:-8:-2])
# print(str[-11:-6])
# print(str[-3:-11:-3])
# print(str[::])
# print(str[::2])
# print(str[-13:13])
# print(str[::-1])
# print(str[-3:5:-1])
# print(str[3::3])
# print(str[2:6:0])

# str1="Shrinu"
# str2="Shreya"
# str3=str1+str2
# print(str3)
#
# # str4=str1-str2       not support
#
# str5=str1*3
# print(str5)

# str6=str1/str2   not support

# Str=input("Enter a String")
# ans_str=""
# for i in Str:
#     if i not in ans_str:
#         ans_str+=i
# print(ans_str)

# strip() --------- method
# str="   Abhi    "
# print(str.lstrip())
# print(str.rstrip())
# print(str.strip())


# str="   Reddy  is  Drinking    "
# ans_str=""
# for  i in str:
#     if i!=" ":
#         ans_str=ans_str+i
# print(ans_str)


# Str=input("Enter a String")
# str1=""
# str2=Str.split()
# for i in str2:
#     # str1=i+str1
#     str1=i+" "+str1
#
# print(str1)


# str=input("Enter a String")
#
# if str.isalpha():
#     print("String contains only Alphabets")
# elif str.isdigit():
#     print("String contains only numbers")
# elif str.isalnum():
#     print("String contains both")
# else:
#     print("Other characters")

str="Rama"
print(str.upper())
print(str.lower())
print(str.swapcase())

str1="Rama"  #packing
r1,r2,r3,r4=str  #unpacking
print(r1)
print(r2)
print(r3)
print(r4)




