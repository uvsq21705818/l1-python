import random as rd

two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9
ten = 10
jack = 10
queen = 10
king = 10
ace_low = 1 
ace_high = 11
ace = 0

l = [two, three, four, five, six, seven, eight, nine, ten, jack, queen, king, ace]

card1 = rd.choice(l)
card2 = rd.choice(l)

if card1 == ace and card2 + ace_high <= 21:
    card1 = ace_high
elif card1 == ace and card2 + ace_high <= 21:
    card1 = ace_low

if card2 == ace and card1 + ace_high <= 21:
    card2 = ace_high
elif card2 == ace and card1 + ace_high > 21:
    card2 = ace_low

n = card1 + card2

if 21 >= n > 16:
    print("stay")
    print(card1, card2)
elif n < 16:
    n += rd.randint(1, 11)
    print(card1, card2)
elif n > 21:
    print("burn")
    print(n)