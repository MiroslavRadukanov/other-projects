innums = [int(x) for x in input().split()]
even = [] 
odd = []
for num in innums:
  if num%2==0:
    even.append(num)
  else:
    odd.append(num)

print(even, "Sum of even nums:", sum(even))
print(odd, "Sum of odd nums:", sum(odd))
    
