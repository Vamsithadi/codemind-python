a,b,c=map(int,input().split())
k=""
a=(2*a*b*c*512)//1024
k+=str(a)
k+="KB"
print(k)