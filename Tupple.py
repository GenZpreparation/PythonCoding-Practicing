
# print(t[0])
# m=t[0]
# for i in t:
#     m=max(i,m)
# print(m)


# print(tuple(set(t)))

# frequency={}
# for i in t:
#     if i not in frequency:
#         frequency[i]=1
#     else:
#         v=frequency[i]
#         frequency[i]=v+1
#
# print(frequency)
#
# first_largest=float('-inf')
# second_largest=float('-inf')
#
# for i in t:
#     if i>first_largest:
#         second_largest=first_largest
#         first_largest=i
#     elif i>second_largest and i!=first_largest:
#         second_largest=i
#
# print(first_largest)
# print(second_largest)



t1=(1,2,3,4)
t2=(2,5,6,7,8)
merge=[]

for i in t1:
    merge.append(i)
for i in t2:
    merge.append(i)

print(merge)

print(sorted(t1))

print(max(t1))





