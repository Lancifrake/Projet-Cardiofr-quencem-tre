
import csv

def Traitement_donnees():

    class Memoire(object):
        """ Creation de la classe pour le stockage des informations du  fichier .csv """

    stockage = Memoire()
    stockage.lecture_donnees = []
    fichier = open("C:\\Users\\fokow\\Desktop\\Ecole\\Dossier\\COURS\\Fondamentaux scientifique\\Projet\\New folder\\Module4\\Programme python\\test",encoding="utf-8-sig")
    fichiercsv = csv.reader(fichier)
    for ligne in fichiercsv:
        stockage.lecture_donnees.append(ligne)
        
   
    tableau=stockage.lecture_donnees
    tableau.remove(tableau[0])

    return tableau