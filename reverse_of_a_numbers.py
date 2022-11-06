n=int(input())
r=0
while n:
    a=n%10
    r=r*10+a
    n=n//10
print(r)    