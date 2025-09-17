import random

def hand_value(cards):
    total = 0
    aces = 0
    for c in cards:
        if c in ["J", "Q", "K"]:
            total += 10
        elif c == "A":
            total += 11
            aces += 1
        else:
            total += c

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def draw_card(deck):
    return deck.pop()

def new_deck():
    deck = []
    for rank in [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]:
        deck.extend([rank]*4)
    random.shuffle(deck)
    return deck

p1chips = 100000
p2chips = 100000

while p1chips > 0 and p2chips > 0:
    chipsin = int(input(f"You have {p1chips} chips. How many do you want to bet? "))
    while chipsin > p1chips or chipsin <= 0:
        print("Invalid bet.")
        chipsin = int(input("How many chips do you want to bet? "))

    
    deck = new_deck()

    
    cards1 = [draw_card(deck), draw_card(deck)]
    cards2 = [draw_card(deck), draw_card(deck)]

    sum1 = hand_value(cards1)
    sum2 = hand_value(cards2)

    print(f"P1 cards: {cards1}, sum = {sum1}")
    print(f"P2 shows: {cards2[0]}")

    
    if sum1 == 21 and sum2 == 21:
        print("Both players have Blackjack! Draw!")
  
