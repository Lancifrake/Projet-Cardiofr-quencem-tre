# Importation du module Tkinter

from tkinter import *
import os


## Initialisation d'un changement de fenetre

def changer():
    interface.destroy()
    os.popen("python Interface\ordre_fichier.py")
def changer1():
    interface.destroy()
    os.popen("python Interface\main3.py")
def changer2():
    interface.destroy()
    os.popen("python Interface\main4.py")
def changer_q():
    interface.destroy()
    os.popen("python Interface\main1.py")





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

image=PhotoImage(file="logo\logo.png")
canevas=Canvas(boite,width=200,height=200,bg="pink")
canevas.create_image(100,100,image=image)
canevas.pack()
boite.pack(fill=X)

## Creation d'une seconde Frame pour stocker les boutons 
boite_2=Frame(interface,bg="pink")
label_title=Label(boite_2,text="Veiller choisir l'ordre", font=("calibri",30),bg="pink")
label_title.pack(expand=YES)

## Creation d'une sous-Frame
sous_boite=Frame(boite_2,bg="pink",width=300)
padding=200

## Creation des boutons de selections

    # Premier

bouton_1=Button(sous_boite,text="Ordre du fichier", font=("calibri",30),bg="pink",width=20,height=3,command=changer)
bouton_1.grid(row=0,column=0,sticky=W)

    # Deuxieme

bouton_2=Button(sous_boite,text="Ordre croissant", font=("calibri",30),bg="pink",width=20,height=3,command=changer1)
bouton_2.grid(row=1,column=0,sticky=W)

    # Troisieme

bouton_3=Button(sous_boite,text="Ordre decroissant", font=("calibri",30),bg="pink",width=20,height=3,command=changer2)
bouton_3.grid(row=2,column=0,sticky=W)




sous_boite.pack()

## Creation d'un bouton de fermeture de l'interface

bouton_fermeture=Button(boite_2,text="QUITTER", font=("calibri",30),bg="pink",width=10,command=changer_q)
bouton_fermeture.pack(side=RIGHT)


boite_2.pack(expand=YES)



interface.mainloop()




