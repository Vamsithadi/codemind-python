n=input()
l=list(map(int,input().split()))
c=[]
for i in l:
    if i not in c:
        c.append(i)
for i in c:
    a=l.count(i)
    print(i,a,end=' ')