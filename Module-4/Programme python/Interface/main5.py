# Importation du module Tkinter

from tkinter import *
import os


## Initialisation d'un changement de fenetre

def changer_q():
    interface.destroy()
    os.popen("python Interface\main1.py")


# Creation de l'interface
interface = Tk()

# Personnalisation de l'interface

interface.title("Coeur de LEDs")    # Changement du titre de la fenetre
interface.geometry("1920x1080")      # Reglage de la taille par defaut de l'interface
interface.iconbitmap("logo\logo.ico")    # Ajout d'une icone a l'application
interface.config(background="pink") # Changer la couleur d'arriere plan de l'interface

## Creation d'une Frame principale
frame=Frame(interface,bg="pink")

## Creation d'une Frame
boite=Frame(interface, bg="pink")

image=PhotoImage(file="logo\logo.png")
canevas=Canvas(boite,width=200,height=200,bg="pink")
canevas.create_image(100,100,image=image)
canevas.pack()
boite.pack(fill=X)

## Creation d'une seconde Frame pour stocker les boutons 
boite_2=Frame(interface,bg="pink")
label_title=Label(boite_2,text="Veillez choisir la valeur a afficher", font=("calibri",30),bg="pink")
label_title.pack(expand=YES)

## Creation d'une sous-Frame
sous_boite=Frame(boite_2,bg="pink",width=300)
padding=200

## Creation des boutons de selections

    # Premier

bouton_1=Button(sous_boite,text="min", font=("calibri",30),bg="pink",width=20,height=3)
bouton_1.grid(row=0,column=0,sticky=W)

    # Deuxieme
bouton_1=Button(sous_boite,text="max", font=("calibri",30),bg="pink",width=20,height=3)
bouton_1.grid(row=1,column=0,sticky=W)





sous_boite.pack()

## Creation d'un bouton de fermeture de l'interface

bouton_fermeture=Button(boite_2,text="QUITTER", font=("calibri",30),bg="pink",width=10,command=changer_q)
bouton_fermeture.pack(side=RIGHT)


boite_2.pack(expand=YES)



interface.mainloop()




