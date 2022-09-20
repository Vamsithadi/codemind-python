def pm(a):
    if a==1 or a<0:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True        
def pn(a):
    c=0
    x=a.index(max(a))
    y=a.index(min(a))
    if x>y:
        for i in range(y,x+1):
            if pm(a[i]):
                c+=1
    else:
        for i in range(y,x-1,-1):
            if pm(a[i]):
                c+=1
    return c            
n=int(input())
l=list(map(int,input().split()))
print(pn(l))