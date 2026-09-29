List = [2, 7, 11, 15, 3, 6]
Target = 21
ans=[]
for i in range(0,len(List)):
    d=Target-List[i]
    if d in List[i+1:]:
        idx=List[i+1:].index(d)
        ans.append(i)
        ans.append(idx+i+1)
        break

print(ans)

