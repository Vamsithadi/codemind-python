def po(n):
  c=[]
  for i in range(n):
    d=2**i
    c.append(d)
  if n in c:
    return 0
  g=[]
  for i in c:
    g.append(abs(n-i))
  return min(g)

v=int(input())
print(po(v))