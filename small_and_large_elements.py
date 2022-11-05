def sl(n):
    l=[]
    l.append(min(n[0]))
    l.append(max(n[-1]))
    return l
a=input()
a.lower()
a=a.split()
print(*sl(a))
