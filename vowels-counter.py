text = input()
count = 0
vowels = "aoeiu"

for ch in text.lower():
    if ch in vowels:
      count += 1

print(count)
