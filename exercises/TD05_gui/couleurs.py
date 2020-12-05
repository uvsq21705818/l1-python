import tkinter as tk
import random as rd

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color):
    canvas.create_line((i, j), (i+1, j), fill=color)
    return

def ecran_aleatoire():

    for i in range (0, canvas_width):
        for j in range (0, canvas_width):
            color = get_color(rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))
            draw_pixel(j, i, color)

def degrade_gris():

    x = 0
    for i in range (0, canvas_width):
        color = get_color(255 - x, 255 - x, 255 - x)
        for j in range (0, canvas_width):
            draw_pixel(canvas_height - x, j, color)
        x +=1

def degrade_2d():
    x = 0
    y = 0
    for i in range (0, canvas_width):
        y += 1
        for j in range (0, canvas_width):
            color = get_color(y, 0, x)
            draw_pixel(i, j, color)
            x +=1
            if x>255:
                x = 0

root = tk.Tk()

bouton_aleatoire = tk.Button(root, text="Aléatoire", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=ecran_aleatoire)
bouton_gris_deg = tk.Button(root, text="Dégradé gris", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=degrade_gris)
bouton_gris_2d = tk.Button(root, text="Dégradé 2d", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=degrade_2d)

canvas_height = 256
canvas_width = 256

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black", bd=10, relief="raised")

bouton_aleatoire.grid(column=0, row=1)
bouton_gris_deg.grid(column=0, row=2)
bouton_gris_2d.grid(column=0, row=3)

canvas.grid(column=1, row=1, rowspan=3)

root.mainloop()