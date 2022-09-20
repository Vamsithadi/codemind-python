def rv(a):
    r=0
    while a:
        b=a%10
        r=r*10+b
        a=a//10
    return r    
n=int(input())
l=list(map(int,input().split()))
for i in l:
    print(rv(i),end=' ')
    