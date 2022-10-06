s=str(input())
s=s.casefold()
if s==s[::-1]:
    print(True)
else:
    print(False)