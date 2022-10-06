def ang(s):
    l=[]
    for i in s.lower():
        l.append(i)
    d={}
    for i in l:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
a=str(input())
b=str(input())
if ang(a)==ang(b):
    print(True)
else:
    print(False)
            
        
  