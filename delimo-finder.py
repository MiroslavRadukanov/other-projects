n = int(input("Naj-golqmo chislo: "))
i = 1
delitel = int(input("Delitel: "))
list = []
listnum = []
while i <= n:
  if i%delitel==0:
    listnum.append(i)
  i += 1
print(listnum)
