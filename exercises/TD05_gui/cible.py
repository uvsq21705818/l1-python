import tkinter as tk

COTE = 500
nb_cercle = 30
colors = ["blue", "green", "black", "yellow", "magenta", "red"]

root = tk.Tk()
canvas = tk.Canvas(root, width = COTE, height = COTE, bg="black")
canvas.grid()

epaisseur = (COTE // 2) // nb_cercle

for i in range(nb_cercle):
    canvas.create_oval((epaisseur*i, epaisseur*i), (COTE-epaisseur*i, COTE-epaisseur*i), fill=colors[i % len(colors)], outline=colors[i % len(colors)])
root.mainloop()