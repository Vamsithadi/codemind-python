def sl(a):
    l=[]
    for i in a:
        l.append(min(i))
        l.append(max(i))
    return l
n=input ()
n.lower()
n=n.split()
print(*sl(n))