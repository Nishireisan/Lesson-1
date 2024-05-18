pal = str(input())
n = len(pal)
print(pal[4] + pal[3] + pal[2] + pal[1] + pal[0])


slovo = str(input())
n1 = len(slovo)
pol = str(slovo[n1-1])
while n1 > 1:
    pol += str(slovo[n1-2])
    n1 -= 1
else:
    print(pol)
