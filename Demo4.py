dic1={
    "name":"Abhishek",
    "age":23
}

dic2={
    "clg":"TIT",
    "place":"Bhopal",
    "name":"Abhishek",
    "age":23
}


li=[]
for i in dic1:
    if i in dic2:
        li.append(i)

print(li)


