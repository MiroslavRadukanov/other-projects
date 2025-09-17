nums = [int(x) for x in input().split()]
nums4 = []

for num in nums:
  if num % 4 == 0:
    nums4.append(num)

print(nums4, sum(nums4), len(nums4))
