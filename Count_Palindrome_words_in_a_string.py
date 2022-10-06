def ip(n):
    n=n.casefold()
    if n==n[::-1]:
        return True
    else:
        return False
s=str(input())
a=s.split(" ")
c=0
for i in a:
    if ip(i)==True:
        c+=1
print(c)        
        
