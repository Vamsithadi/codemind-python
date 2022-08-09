n=int(input())
a=[]
c=0
while n:
   r=n%10
   n=n//10
   c+=r
   a.append(r)
b=set(a)
if sum(b)==c:
    print("Unique Number")
else:
    print("Not Unique Number")
   