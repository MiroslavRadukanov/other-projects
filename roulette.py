import random

chips = 1000

while chips > 0:
    choice = int(input("Coded by Miro! Choose in what you want to bet - on a number (1) or on a color (2)? "))
    bet = int(input(f"You have {chips} chips! Amount of chips you want to bet: "))

    if bet > chips:
        print("You don't have enough chips!")
        continue

    chips -= bet

    result = random.randint(1, 36)
    color = "red" if result % 2 == 0 else "black"

    if choice == 1:
        num = int(input("Select a number from 1 to 36 to bet on: "))
        if num == result:
            print(f"The number stopped at your number - {result} {color}. You won {36*bet} chips.")
            chips += 36*bet + bet 
        else:
            print(f"The number was {result} {color}. You lost {bet} chips.")

    elif choice == 2:
        betcolor = input("What color will you bet on - red or black? ").lower()
        if betcolor == color:
            print(f"Congrats! The number was {result} {color}! You won {bet} chips!")
            chips += 2*bet 
        else:
            print(f"The number was {result} {color}. You lost {bet} chips!")

print("Game over!")
