List = [1, 5, 3, 4, 2]
K = 2

ans=[]

for i in List:
    d=K+i
    if d in List:
        ans.append((i,d))

print(ans)
