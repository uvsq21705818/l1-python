def syracuse(n):
    l = []
    while n != 1:
        if n % 2 == 0:
            n /= 2
            l.append(int(n))
        else:
            n = (n * 3) + 1
            l.append(int(n))
    return l

#print(syracuse(3))

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """

    for i in range(1, n_max):
        syracuse(i)
    return n_max

#print(testeConjecture(10000))

def tempsVol(n):
    """ Retourne le temps de vol de n """
    
    n = len(syracuse(n))
    return n

print("Le temps de vol de", 3, "est", tempsVol(3))