n=input()
m=list(map(int,input().split()))
c=[]
d=[]
for i in m:
    if i%2==0:
        c.append(i)
    if i%2==1:
        d.append(i)
if len(d)>=1:
    print(False)
else:
    print(True)