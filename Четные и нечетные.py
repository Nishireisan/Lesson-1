slovo = str(input())
n = len(slovo)
print(n)
      #четное
chet = str()
while n > 0:
    chet += str(slovo[n-1])
    n -= 2
else:
    print(chet)
    # полиндром 1
n1 = len(chet)
chet1 = str(chet[n1-1])
while n1 > 1:
    chet1 += str(chet[n1-2])
    n1 -= 1
else:
    print(chet1)

    #нечетное
nech = str()
n2 = len(slovo) - 1
while n2 > 0:
    nech += str(slovo[n2-1])
    n2 -= 2
else:
    print(nech)
         #полиндром 2
n3 = len(nech)
nech1 = str(nech[n3-1])
while n3 > 1:
    nech1 += str(nech[n3-2])
    n3 -= 1
else:
    print(nech1)

print(chet1 + ' ' + nech1) #ИТОГ
