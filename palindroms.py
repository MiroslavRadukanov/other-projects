nums = [x for x in input().split()]
have = False
palind = 0
palindnum = []

for num in nums:
  if num == num [::-1]:
    print("Palindrome:", num)
    have = True
    palind += 1
    palindnum.append(int(num))

if have == True:
  print(f"There were {len(palindnum)} palindromes with sum {sum(palindnum)} and average {sum(palindnum) / len(palindnum)}.")

if have == False:
  print("No palindromes!")

