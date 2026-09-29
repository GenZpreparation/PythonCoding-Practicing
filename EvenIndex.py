import collections as c

list=[1,2,3,4,5,1,2,1,5,6,2,3,3,3,1]

list_count=c.Counter(list)

for i in list_count:
    print(f"{i} -> {list_count[i]}")
