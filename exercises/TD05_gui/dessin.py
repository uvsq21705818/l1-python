import tkinter as tk
import random as rd

def couleur():
    global color
    color = input("Choisir une couleur\n")

def cercle():
    x = rd.randint(0, 401)
    y = rd.randint(0, 401)
    canvas.create_oval((x, y), (x+100, y+100), fill=color)

def carre():
    x = rd.randint(0, 401)
    y = rd.randint(0, 401)
    canvas.create_rectangle((x, y), (x+100, y+100), fill=color)

def croix():
    x = rd.randint(0, 401)
    y = rd.randint(0, 401)
    canvas.create_line((x, y), (x+100, y+100), fill=color)
    canvas.create_line((x+100, y), (x, y+100), fill=color)

root = tk.Tk()
root.title("Dessin")
color = "blue"

bouton_couleur = tk.Button(root, text="Choisir une couleur", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=couleur)
bouton_cercle = tk.Button(root, text="Cercle", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=cercle)
bouton_carre = tk.Button(root, text="Carré", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=carre)
bouton_croix = tk.Button(root, text="Croix", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=croix)

canvas = tk.Canvas(root, width=500, height=500, bg="black", bd=10, relief="raised")

bouton_couleur.grid(column=1, row=0)
bouton_cercle.grid(column=0, row=1)
bouton_carre.grid(column=0, row=2)
bouton_croix.grid(column=0, row=3)

canvas.grid(column=1, row=1, rowspan=3)

root.mainloop()
