import math

nums = [int(x) for x in input().split()]  
perfect_squares = []

for num in nums:
    if math.isqrt(num)**2 == num:       perfect_squares.append(num)

print(perfect_squares, sum(perfect_squares), len(perfect_squares))
