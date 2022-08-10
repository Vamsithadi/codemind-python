def sd(n):
    z=n
    c=0
    d=0
    e=0
    while n!=0:
        a=n%10
        if a==0:
            c+=1
            break
        d+=1
        if z%a==0:
            e+=1
        n=n//10    
    if d==e and c==0:
        return True
    else:
        return False
a=int(input())        
b=int(input())
for i in range(a,b+1):
    if sd(i)==True:
        print(i,end=' ')