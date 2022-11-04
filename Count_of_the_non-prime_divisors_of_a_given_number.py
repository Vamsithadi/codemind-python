def pm(a):
    f=0
    if a==1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            f+=1
    if f==0:
        return True
    return False    
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0 and pm(i)==False:
        c+=1
print(c)        