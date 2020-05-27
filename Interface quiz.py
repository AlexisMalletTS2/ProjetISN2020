import tkinter as tk
from tkinter.font import *
from random import *

fenetre = tk.Tk()
fenetre.title("L'Heure Des Questions")
fenetre.geometry("481x600")
fenetre.configure(bg = "black")

Bouton1 = tk.Button(fenetre, text = "Réponse 1", height = 8, width = 20, activebackground ="light gray")
Bouton1.place (x = 60, y = 270)
Bouton2 = tk.Button(fenetre, text = "Réponse 2", height = 8, width = 20, activebackground ="light gray")
Bouton2.place (x = 280, y = 270)
Bouton3 = tk.Button(fenetre, text = "Réponse 3", height = 8, width = 20, activebackground ="light gray")
Bouton3.place (x = 60, y = 450)
Bouton4 = tk.Button(fenetre, text = "Réponse 4", height = 8, width = 20, activebackground ="light gray")
Bouton4.place (x = 280, y = 450)


L = tk.Label(fenetre, text = 'BIENVENUE DANS LE CERCLE DE L AMITIE', fg = 'white', font = 'times', background = 'black')
L.place(x = 20, y = 15)

fenetre.mainloop()