stroka = str(input())
n = len(stroka)
print(n)
if (n/2) > float(n//2):
    k = n//2+1
else:
    k = n//2

print(stroka[k:n] + stroka[:k])
