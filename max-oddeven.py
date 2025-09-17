nums = [int(x) for x in input().split()]

odd = []
even = []

for num in nums:
  if num%2 == 0:
    even.append(num)
  else:
    odd.append(num)

print(max(odd), min(even), max(odd)-min(even))
