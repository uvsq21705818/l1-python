import tkinter as tk
import random as rd

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def draw_pixel(i, j, color="white"):
    """ affiche le pixel de coordonnées (i,j) dans le canevas avec la couleur color """
    toto.create_line((i, j), (i+1, j), fill=color)
    
def aleatoire():
    for j in range(256):
        for i in range(256):
            r = rd.randint(0, 255)
            g = rd.randint(0, 255)
            b = rd.randint(0, 255)
            col = get_color(r, g, b)
            draw_pixel(i, j, col)

def degrade_gris():
    for j in range(256):
        col = get_color(j ,j, j)
        toto.create_line((j, 0), (j, 256), fill=col)

def degrade_2d():
    for j in range(256):
        for i in range(256):
            col = get_color(0, i, j)
            draw_pixel(j, i, color=col)




racine = tk.Tk()
racine.title("Mon dessin")
# création des widgets
bouton_alea = tk.Button(racine, text="Aléatoire", bg="grey100", fg="blue", padx=20, font=("Times", "26"), command=aleatoire)
bouton_gris = tk.Button(racine, text="Dégradé gris", bg="grey100", fg="blue", padx=20, font=("Times", "26"), command=degrade_gris)
bouton_2d = tk.Button(racine, text="Dégradé 2D", bg="grey100", fg="blue", padx=20, font=("Times", "26"), command=degrade_2d)
toto = tk.Canvas(racine, width=256, height=256, bg="black")
#col = get_color(10, 251, 123)
#draw_pixel(128, 128, col)

# placement des widgets
bouton_alea.grid(column=0, row=0)
bouton_gris.grid(column=0, row=1)
bouton_2d.grid(column=0, row=2)
toto.grid(column=1, row=0, rowspan=3)
racine.mainloop()