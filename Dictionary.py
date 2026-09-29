S="abhishekssoni"
frequency={}
for i in S:
    if i not in frequency:
        frequency[i]=1
    else:
        v=frequency[i]
        frequency[i]=v+1
print(frequency)

print(frequency.keys())
k=""
f=0
for i in frequency.keys():
    if frequency[i]>f:
        k=i
        f=frequency[i]

print(k)
print(f)

fre={
    'name':"Abhishek",
    'cast':'Soni'
}
# print(frequency.values())