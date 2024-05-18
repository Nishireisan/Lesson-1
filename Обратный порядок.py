slovo = str(input())
n = len(slovo)
      #четное
chet = str(slovo[n-2])
n -= 2
while n > 1:
    chet += str(slovo[n-1])
    n -= 1
else:
    print(chet)
