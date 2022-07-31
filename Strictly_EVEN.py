n=int(input())
m=list(map(int,input().split()))
c=0
d=0
for i in m:
    if i%2==0:
        c+=1
for j in range(n):
    if j%2==0 and m[j]%2==0:
        d+=1
print(c==d)
