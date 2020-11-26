import random as rd

def affichePair(n):
    if n % 2 == 0:
        print(n, "Pair\n")
    else:
        print(n, "Impair\n")
    return n

nombre = rd.randint(1, 100)

print(affichePair(nombre))