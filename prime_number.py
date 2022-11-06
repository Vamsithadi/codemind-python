def pm(n):
    c=0
    if n==1:
        return "not a prime"
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            c+=1
    if c==0:
        return "prime"
    return "not a prime"    
a=int(input())    
print(pm(a))