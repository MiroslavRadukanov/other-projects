num = [float(x) for x in input().split()]
nums = list(set(num))
nums.sort()

lnum = nums[-1]
l2num = nums[-2]
ssum = lnum + l2num
print(lnum, l2num, ssum)
