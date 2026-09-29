# min value in List
# list=[1,2,6,3,9,6,0]
# m=list[0]
# for i in list:
#     m=min(i,m)
#
# print(m)
from setuptools.discovery import remove_stubs

# list=[1,4,6,2,3]
# sum=0
# for i in list:
#     sum+=i
#
# print(sum/len(list))
#

# list=[1,4,6,2,3]
#
# i=0
# j=len(list) - 1
# while i<j:
#     a=list[i]
#     list[i]=list[j]
#     list[j]=a
#     i+=1
#     j-=1
#
# print(list)

# c=0
# for i in list:
#     c+=1
# print(c)
#


# list=[1,5,6,7,3,4,2,3,5,3,8,3]
# n=3
#
# c=0
# for i in list:
#     if i==n:
#         c+=1
# print(c)

# list=[1,2,4,6,3,9]
# n=0
# # print(n in list)
# for i in list:
#     if i==n:
#         print("True")
#         break
#

#
# list=[1,4,6,7,2,3,0,4]
# first_largest=float('-inf')
# second_largest=float('-inf')
#
# for num in list:
#     if num >first_largest:
#         second_largest=first_largest
#         first_largest=num
#     elif num>second_largest and num!=first_largest:
#         second_largest=num
#
# print(first_largest)
# print(second_largest)

# lis=[1,2,4,7,2,4,9,8,1]
# lis=[1,2,4,7,9,8]
# li=list(set(lis))
# print(li)
#
# lis.sort()
# i=0
# ans_list=[]
# for i in range(0,len(lis)-1):
#     if lis[i]==lis[i+1]:
#         if lis[i] not in ans_list:
#              ans_list.append(lis[i])
#     i+=1
#
# print(ans_list)
#

# numbers=[1,6,7,2,8,0,4,8,2,5]
# odd_list=[]
# even_list=[]
#
# for i in numbers:
#     if i%2==0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
#
# print(even_list)
# print(odd_list)


# numbers1=[1,6,7,12,4,18,2,5]
# numbers2=[1,7,2,8,0,4,8,2,5]
# ans_list=[]
# for i in numbers1:
#     if i in numbers2:
#         ans_list.append(i)
#
# print(ans_list)

# for i in numbers1:
#     if i not in numbers2:
#         numbers2.append(i)
#
# print(numbers2)

# n1=1
# n2=10
# numbers=[1,2,3,4,6,7,8,9,10]
#
# exact_sum=int((n2*(n2+1))/2)
# sum=0
# for i in numbers:
#     sum+=i
# print(exact_sum-sum)
# numbers=[0,1,2,0,3,0,4,6]
# i=0
# p=0
# for i in range(0,len(numbers)):
#     if numbers[i]!=0:
#         numbers[p]=numbers[i]
#         p+=1
#
# while p<len(numbers):
#     numbers[p]=0
#     p+=1
# print(numbers)
#
#

# numbers=[1,2,3,4,6,7,8,9,10]
#
# t=7
# i=0
# for i in range(0,len(numbers)):
#     d=t-numbers[i]
#     if d in numbers:
#         print([i,numbers.index(d)])
#         break











