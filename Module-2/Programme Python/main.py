from tkinter import *   # Importation du module Tkinter pour la conception de l'interface graphique
import os               # Importation du module os

from menu import *      # Importer toutes les fonctions du module menu pour les utiliser


## Initialisation d'un changement de fenetre
def changer():
    interface.destroy()
    os.popen("python choix.py")


# Creation de l'interface
interface = Tk()

# Personnalisation de l'interface

interface.title("Coeur de LEDs")    # Changement du titre de la fenetre
interface.geometry("1200x700")      # Reglage de la taille par defaut de l'interface
interface.iconbitmap("logo\logo.ico")    # Ajout d'une icone a l'application
interface.config(background="pink") # Changer la couleur d'arriere plan de l'interface

## Creation d'une Frame principale
frame=Frame(interface,bg="pink")

## Creation d'une Frame
boite=Frame(interface, bg="pink")

image=PhotoImage(file="logo\logo.PNG")
canevas=Canvas(boite,width=200,height=200,bg="pink")
canevas.create_image(100,100,image=image)
canevas.pack()
boite.pack(fill=X)

## Creation d'une seconde Frame pour stocker les boutons 
boite_2=Frame(interface,bg="pink")
label_title=Label(boite_2,text="Quelle configuration souhaitez-vous utiliser pour alumer les LED", font=("calibri",30),bg="pink")
label_title.pack(expand=YES)

## Creation d'une sous-Frame
sous_boite=Frame(boite_2,bg="pink",width=300)
padding=200

## Creation des boutons de selections

    # Premier

bouton_1=Button(sous_boite,text="1 LED sur 2", font=("calibri",30),bg="pink",width=20,command=UneLEDsurdeux)
bouton_1.grid(row=0,column=0,sticky=W)



    # Deuxieme

bouton_2=Button(sous_boite,text="1 LED sur 3", font=("calibri",30),bg="pink",width=20,command=UneLEDsurtrois)
bouton_2.grid(row=0,column=1,sticky=W)


    # Troisieme

bouton_3=Button(sous_boite,text="Mode CHENILLE", font=("calibri",30),bg="pink",width=20,command=Modechenille)
bouton_3.grid(row=1,column=0,sticky=W)


    # Quatrieme

bouton_4=Button(sous_boite,text="Choix de la LED", font=("calibri",30),bg="pink",width=20,command=changer)
bouton_4.grid(row=1,column=1,sticky=W)


    # Cinquieme

bouton_5=Button(sous_boite,text="Mode TRANSITION", font=("calibri",30),bg="pink",width=20,command=Modetransition)
bouton_5.grid(row=2,column=0,sticky=W)



sous_boite.pack()

## Creation d'un bouton de fermeture de l'interface

bouton_fermeture=Button(boite_2,text="QUITTER", font=("calibri",30),bg="pink",width=10,command=interface.quit)
bouton_fermeture.pack(side=RIGHT)


boite_2.pack(expand=YES)



interface.mainloop()



