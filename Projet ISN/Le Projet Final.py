import tkinter as tk                     # le programme va aller chercher toutes les fonctions de la bibliothèque Tkinter
from tkinter.font import *
from PIL import Image, ImageTk

def deplacement():                        #Tentative de fonction de déplacement d'image
    canvas_dep.move(pirouette7,0,5)



def nouvfen():                          #Création d'une nouvelle fenêtre sous la forme d'une fonction

    fenetre.destroy()               #Destruction de la précédente
    global fenetre2
    fenetre2 = tk.Tk()
    fenetre2.title("Le cercle de l'amitié")     #Titre de la fenêtre
    fenetre2.geometry("481x600")                #Taille de la fenêtre
    fenetre2.minsize(481,600)                   #Taille minimale
    fenetre2.maxsize(481,600)                   #Taille maximale
    fenetre2.config(bg = "#798081")             #Couleur de fond


    Grille = tk.Canvas(fenetre2,height=480,width=480)                   #Création d'une grille sous la forme d'un canvas
    Grille.pack()
    carreau=[[Grille.create_rectangle(i*32,j*32,(i+1)*32,(j+1)*32,fill="#D2CAEC")
    for i in range(15)] for j in range(15)]

    B_exit = tk.Button (fenetre2, text = "Quitter le Jeu" , command = fenetre2.destroy , activebackground = "#FEA347" , bg = "#A9EAFE" )    #Création d'un bouton
    B_exit.place(x = 380, y = 530)

    B_depart = tk.Button (fenetre2, text = "Commencer", command = deplacement, activebackground = "#FEA347" , bg = "#A9EAFE" )               #Création d'un bouton
    B_depart.place(x= 300, y = 530)

    L_score = tk.Label(fenetre2, text ="Votre cercle d'Amitié :", fg = "#EE1010", bg = "#798081")                   #Création d'un label
    L_score.place(x = 30, y = 500)

    L_TimeAfterQuest = tk.Label(fenetre2, text ="Nombre de coeur à avaler avant votre question :", fg = "#EE1010", bg = "#798081")  #Création d'un label
    L_TimeAfterQuest.place(x = 30, y = 530)

    pirouette1=Image.open("E:/ISN/Projet ISN/1Pirouette32x32.png")      #Importation d'une image
    photoImage=ImageTk.PhotoImage(pirouette1)
    Labelimage2=tk.Label(fenetre2, image=photoImage)
    Labelimage2.image = photoImage
    Labelimage2.place(x=66,y=66)
    Labelimage2.configure(bg="#D2CAEC")

    pirouette2=Image.open("E:/ISN/Projet ISN/2Pirouette32x32.png")      #Importation d'une image
    photoImage=ImageTk.PhotoImage(pirouette2)
    Labelimage2=tk.Label(fenetre2, image=photoImage)
    Labelimage2.image = photoImage
    Labelimage2.place(x=66,y=66)
    Labelimage2.configure(bg="#D2CAEC")

    pirouette3=Image.open("E:/ISN/Projet ISN/3Pirouette32x32.png")      #Importation d'une image
    photoImage=ImageTk.PhotoImage(pirouette3)
    Labelimage2=tk.Label(fenetre2, image=photoImage)
    Labelimage2.image = photoImage
    Labelimage2.place(x=66,y=66)
    Labelimage2.configure(bg="#D2CAEC")

    pirouette4=Image.open("E:/ISN/Projet ISN/4Pirouette32x32.png")      #Importation d'une image
    photoImage=ImageTk.PhotoImage(pirouette4)
    Labelimage2=tk.Label(fenetre2, image=photoImage)
    Labelimage2.image = photoImage
    Labelimage2.place(x=66,y=66)
    Labelimage2.configure(bg="#D2CAEC")

    pirouette5=Image.open("E:/ISN/Projet ISN/5Pirouette32x32.png")      #Importation d'une image
    photoImage=ImageTk.PhotoImage(pirouette5)
    Labelimage2=tk.Label(fenetre2, image=photoImage)
    Labelimage2.image = photoImage
    Labelimage2.place(x=66,y=66)
    Labelimage2.configure(bg="#D2CAEC")

    pirouette6=Image.open("E:/ISN/Projet ISN/6Pirouette32x32.png")      #Importation d'une image
    photoImage=ImageTk.PhotoImage(pirouette6)
    Labelimage2=tk.Label(fenetre2, image=photoImage)
    Labelimage2.image = photoImage
    Labelimage2.place(x=66,y=66)
    Labelimage2.configure(bg="#D2CAEC")


    global pirouette7
    pirouette7=Image.open("E:/ISN/Projet ISN/7Pirouette32x32.png")      #Importation d'une image
    photoImage=ImageTk.PhotoImage(pirouette7)
    Labelimage2=tk.Label(fenetre2, image=photoImage)
    Labelimage2.image = photoImage
    Labelimage2.place(x=66,y=66)
    Labelimage2.configure(bg="#D2CAEC")


    global canvas_dep
    canvas_dep=tk.Canvas(fenetre2,width=26,height=26,bd=1,bg="#D2CAEC")
    canvas_dep.pack( padx=66, pady=66)

    pirouette7=canvas_dep.create_image(66,66)


    fenetre2.mainloop()


fenetre = tk.Tk()       #Création de la page d'accueil
fenetre.title("Bienvenue dans Le Jeu")
fenetre.geometry("481x600")
L = tk.Label(fenetre, text = 'BIENVENUE DANS LE CERCLE DE L AMITIE', fg = 'black',font = 'times')
L.place(x = 15, y = 5)
L.configure(bg = "white")
fenetre.configure(bg = "white")

Bouton1 = tk.Button(fenetre, text = "Commencer la Partie", width = 20, activebackground ="light green",command=nouvfen)         #Création d'un bouton
Bouton1.place (x = 165, y = 175)
Bouton2 = tk.Button(fenetre, text = "Quitter Le Jeu", width = 20, command = fenetre.destroy, activebackground ="red")           #Création d'un bouton
Bouton2.place (x = 165, y = 400)

L1 = tk.Label(fenetre, text = "Conçu par Lavie Florian, Fournier Benjamin, Mallet Alexis")
L1.place(x = 90, y = 550)
L1.configure(bg = "white")
coeur = Image.open("F:\ISN\Projet ISN\coeur.png")       #Importation d'une image
photoimage = ImageTk.PhotoImage(coeur)
Labelimage = tk.Label(fenetre, image = photoimage)
Labelimage.image = photoimage
Labelimage.place(x = 130,y = 205)

pirouette1 = Image.open("F:\ISN\Projet ISN\Pirouette1.png")     #Importation d'une image
photoimage = ImageTk.PhotoImage(pirouette1)
Labelimage = tk.Label(fenetre, image = photoimage)
Labelimage.image = photoimage
Labelimage.place(x = 53,y = 100)
Labelimage.configure(bg = "white")

pirouette2 = Image.open("F:\ISN\Projet ISN\Pirouette2.png")     #Importation d'une image
photoimage = ImageTk.PhotoImage(pirouette2)
Labelimage = tk.Label(fenetre, image = photoimage)
Labelimage.image = photoimage
Labelimage.place(x = 50,y = 300)
Labelimage.configure(bg = "white")

pirouette3 = Image.open("F:\ISN\Projet ISN\Pirouette3.png")     #Importation d'une image
photoimage = ImageTk.PhotoImage(pirouette3)
Labelimage = tk.Label(fenetre, image = photoimage)
Labelimage.image = photoimage
Labelimage.place(x = 50,y = 450)
Labelimage.configure(bg = "white")

pirouette4 = Image.open("F:\ISN\Projet ISN\Pirouette4.png")     #Importation d'une image
photoimage = ImageTk.PhotoImage(pirouette4)
Labelimage = tk.Label(fenetre, image = photoimage)
Labelimage.image = photoimage
Labelimage.place(x = 230,y = 450)
Labelimage.configure(bg = "white")

pirouette5 = Image.open("F:\ISN\Projet ISN\Pirouette5.png")     #Importation d'une image
photoimage = ImageTk.PhotoImage(pirouette5)
Labelimage = tk.Label(fenetre, image = photoimage)
Labelimage.image = photoimage
Labelimage.place(x = 415 ,y = 450)
Labelimage.configure(bg = "white")

pirouette6 = Image.open("F:\ISN\Projet ISN\Pirouette6.png")     #Importation d'une image
photoimage = ImageTk.PhotoImage(pirouette6)
Labelimage = tk.Label(fenetre, image = photoimage)
Labelimage.image = photoimage
Labelimage.place(x = 415,y = 300)
Labelimage.configure(bg = "white")

pirouette7 = Image.open("F:\ISN\Projet ISN\Pirouette7.png")     #Importation d'une image
photoimage = ImageTk.PhotoImage(pirouette7)
Labelimage = tk.Label(fenetre, image = photoimage)
Labelimage.image = photoimage
Labelimage.place(x = 415,y = 100)
Labelimage.configure(bg = "white")





fenetre.mainloop()                                                             # lance la boucle principale