nums = [int(x) for x in input().split()]
larger = []

average = sum(nums) / len(nums)

for num in nums:
   if num > average:
      larger.append(num)

print(larger, "Average is", average)
