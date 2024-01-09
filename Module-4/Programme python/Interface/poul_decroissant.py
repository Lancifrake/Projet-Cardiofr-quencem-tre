# Importation du module Tkinter

from tkinter import *
import os

from actions import Poul_decroissant



def afficher():
    resultat = Poul_decroissant()
    ecran.delete(0, END)
    ecran.insert(0,resultat)

## Initialisation d'un changement de fenetre
def changer():
    interface.destroy()
    os.popen("python ...\main.py")

def changer_q():
    interface.destroy()
    os.popen("python Interface\main4.py")



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
label_title=Label(boite_2,text="Resultat", font=("calibri",30),bg="pink")
label_title.pack(expand=YES)

## Creation d'une sous-Frame
sous_boite=Frame(boite_2,bg="pink",width=300)
padding=200


## Creation de l'interface d'affichage du resultat


ecran = Entry(sous_boite,font=("calibri",30),bg="white",fg="black")
ecran.pack(fill=X)

bouton_1=Button(sous_boite,text="Afficher", font=("calibri",30),bg="pink",fg="black",command=afficher)
bouton_1.pack(fill=X)

sous_boite.pack()

## Creation d'un bouton de fermeture de l'interface

bouton_fermeture=Button(boite_2,text="QUITTER", font=("calibri",30),bg="pink",width=10,command=changer_q)
bouton_fermeture.pack(side=RIGHT)


boite_2.pack(expand=YES)



interface.mainloop()





