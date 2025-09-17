def round():
  number = float(input())
  n = int(number)
  f = number - n
  h = 0
  if number >= 0:
    if f >= 0.5:
      h = n + 1
    else:
      h = n
    print(h)
  else:
    if f <= -0.5:
      h = n - 1
    else:
      h = n
    print(h)

round()
