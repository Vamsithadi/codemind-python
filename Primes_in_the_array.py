def pm(n):
    c=0
    for i in range(1,n//2+1):
        if n%i==0:
            c+=1
    if c==1:
        return True
    else:
        return False
a=int(input())        
l=list(map(int,input().split()))
d=0
for i in l:
    if pm(i)==True:
        d+=1
print(d)        
        