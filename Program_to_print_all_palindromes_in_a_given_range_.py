def po(a,b):
  v=[]
  for i in range(a,b+1):
    if mo(i):
      v.append(i)
  return v
  
def mo(a):
  v=co(a)
  f=v[::-1]
  if v==f:
    return True
  else:
    return False

def co(a):
  v=[]
  while a:
    d=a%10
    a=a//10
    v.append(d)
  return v

n=int(input())
m=int(input())
print(*(po(n,m)))