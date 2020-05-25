from tkinter import*
from random import *

fenetre = Tk()
fenetre.title("Snake de questions")
fenetre.geometry("481x600")
fenetre.minsize(481,600)
fenetre.maxsize(481,600)
fenetre.config(bg = "#798081")


Grille = Canvas(fenetre,height=480,width=480)
Grille.pack()
carreau=[[Grille.create_rectangle(i*32,j*32,(i+1)*32,(j+1)*32,fill="#D2CAEC")
for i in range(15)] for j in range(15)]

B_exit = Button (fenetre, text = "Quitter le jeu :'(" , command = fenetre.destroy , activebackground = "#FEA347" , bg = "#A9EAFE" )
B_exit.place(x = 380, y = 530)

L_score = Label(fenetre, text ="Votre cercle d'Amitié :", fg = "#EE1010", bg = "#798081")
L_score.place(x = 30, y = 500)

L_TimeAfterQuest = Label(fenetre, text ="Nombre de coeur à avaler avant votre question :", fg = "#EE1010", bg = "#798081")
L_TimeAfterQuest.place(x = 30, y = 530)

fenetre.mainloop()