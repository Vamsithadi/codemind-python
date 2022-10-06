s=str(input())
l=[]
c=0
for i in s:
    if i not in l:
        l.append(i)
    else:
        c+=1
if c==0:
    print(True)
else:
    print(False)