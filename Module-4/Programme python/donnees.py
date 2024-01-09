
import csv

def Traitement_donnees():

    class Memoire(object):
        """ Creation de la classe pour le stockage des informations du  fichier .csv """

    stockage = Memoire()
    stockage.lecture_donnees = []
    fichier = open("test",encoding="utf-8-sig")
    fichiercsv = csv.reader(fichier)
    for ligne in fichiercsv:
        stockage.lecture_donnees.append(ligne)
        print(ligne)
   
    tableau=stockage.lecture_donnees
    tableau.remove(tableau[0])

    return tableau

a=Traitement_donnees()
print(a)