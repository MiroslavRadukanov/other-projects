import random
import time
chips = 100000
point = 0
want = input(f"Do you want to start the game? You have {chips} chips. (yes/no) ")
while chips != 0 and want == "yes":
  chipsin = int(input(f"How many chips you want to bet? You have {chips} chips. "))
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  sumdice = dice1 + dice2
  print(f"Your dices are {dice1} and {dice2}. The sum is {sumdice}.")
  if sumdice == 7 or sumdice == 11:
    print(f"Congrats! You just won {2*chipsin} chips!")
    chips += chipsin
    continue 
  elif sumdice == 2 or sumdice == 3 or sumdice == 12:
      print(f"You lost {chipsin} chips!")
      chips -= chipsin
  else:
    point = sumdice
    print(f"{sumdice} is your point! If the sum from the next 2 dices is {sumdice}, you win, but if it is 7, you lose!")
    while sumdice != 7 or sumdice == point:
      dice1 = random.randint(1, 6)
      dice2 = random.randint(1, 6)
      sumdice = dice1 + dice2
      print(f"Your dices are {dice1} and {dice2}. The sum is {sumdice}.")
      time.sleep(1)
      if sumdice == 7:
        print(f"The sum was 7. You lost {chipsin} chips!")
        chips -= chipsin
      if sumdice == point:
        print(f"Congrats! You won {chipsin} chips!")
        chips += chipsin
        

  
