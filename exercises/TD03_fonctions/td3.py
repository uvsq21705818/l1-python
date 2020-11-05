#temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    sec = 0
    sec += temps[0] * 24 * 60 * 60
    sec += temps[1] * 60 * 60
    sec += temps[2] * 60
    sec += temps[3]
    return sec

temps = (3,23,1,34)
#print(type(temps))
#print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jour = seconde // (24 * 60 * 60)
    seconde %= (24 * 60 * 60)
    heure = seconde // (60 * 60)
    seconde %= (60 * 60)
    minute = seconde // 60
    seconde %= 60
    return jour, heure, minute, seconde
temps = secondeEnTemps(342094)
#print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

def afficheplur(valeur, unite):
    """Fonction qui affiche le nombre d'unités (heure, jours...) avec le pluriel ou 0 prit en compte"""
    if valeur > 1:
        print(valeur, unite + "s", end=" ")
    elif valeur == 1:
            print(valeur, unite, end=" ")

def afficheTemps(temps):
    afficheplur(temps[0], "jour")
    afficheplur(temps[1], "heure")
    afficheplur(temps[2], "minute")
    afficheplur(temps[3], "seconde")
    print()

#afficheTemps((1,6,14,23))

def demandeTemps():
    jour = int(input("Nombre de jours"))
    heure = int(input("Nombre d'heures"))
    minute = int(input("Nombre de minutes"))
    seconde = int(input("Nombre de de secondes"))
    sec = (jour * 24 * 60 * 60) + (heure * 60 * 60) + (minute * 60) + seconde
    print(sec)
    return jour, heure, minute, seconde, sec

afficheTemps(demandeTemps())