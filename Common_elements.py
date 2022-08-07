a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
x=[]
for i in c:
    for j in d:
        if j==i:
            x.append(j)
z=[]
for y in x:
    if y not in z:
        z.append(y)
print(*z)        
    