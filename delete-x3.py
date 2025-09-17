nums = [int(x) for x in input().split()]
normalnums = []
for num in nums:
  if num%3 == 1 or num%3 == 2:
    normalnums.append(num)

print(normalnums, sum(normalnums))
