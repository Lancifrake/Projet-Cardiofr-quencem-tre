
from donnees import *

###################################################################################################################
###################################################################################################################
##                          Fonctions de tri  des informations du  fichier   .csv                                ##
###################################################################################################################
###################################################################################################################

## Afficher les donnees dans l'ordre du fichier

tableau = Traitement_donnees()


def Ordre_fichier():
    tableau = Traitement_donnees()

    return tableau


## Afficher les donnees dans l'ordre croissant

def Poul_croissant():

    resultat=[]
    i=0
    pouls=[]
    a=0

    while(i<len(tableau)):
        pouls.append(tableau[i][2])
        i=i+1

    pouls.sort()

    i=0

    while(i<len(tableau)):
        while(a<len(pouls) or condition=="false"):
            if(pouls[i]==tableau[a][2]):
                resultat.append(tableau[a])
                condition="true"
            a=a+1
        i=i+1
        a=0
        

    return resultat          

## Afficher les donnees dans l'ordre decroissant

def Poul_decroissant():

    i=0
    a=0
    pouls=[]
    resultat=[]

    while(i<len(tableau)):
        pouls.append(tableau[i][2])
        i=i+1

    pouls.sort(reverse=True)

    i=0

    while(i<len(tableau)):
        while(a<len(pouls) or condition=="false"):
            if(pouls[i]==tableau[a][2]):
                resultat.append(tableau[a])
                condition="true"
            a=a+1
        i=i+1
        a=0
        

    return resultat 


## Afficher les donnees per temps croissant

def Temps_croissant():

    i=0
    a=0
    pouls=[]
    resultat=[]

    while(i<len(tableau)):
        pouls.append(tableau[i][1])
        i=i+1

    pouls.sort()

    i=0

    while(i<len(tableau)):
        while(a<len(pouls) or condition=="false"):
            if(pouls[i]==tableau[a][1]):
                resultat.append(tableau[a])
                condition="true"
            a=a+1
        i=i+1
        a=0
        

    return resultat    

## Afficher les donnees par temps decroissant

def Temps_decroissant():

    i=0
    a=0
    pouls=[]
    condition="false"
    resultat=[]

    while(i<len(tableau)):
        pouls.append(tableau[i][1])
        i=i+1

    pouls.sort(reverse=True)

    i=0

    while(i<len(tableau)):
        while(a<len(pouls) or condition=="false"):
            if(pouls[i]==tableau[a][1]):
                resultat.append(tableau[a])
                condition="true"
            a=a+1
        i=i+1
        a=0
        

    return resultat  

## Affichage du nombres de lignes en memoire

def Nbre_ligne():

    i=0
    compteur=0
    while(i<len(tableau)):
        compteur=compteur+1
        i=i+1
        

    return compteur

## Affichage du Maximum

def Maximum():

    maxi = tableau[0][2]
    i=1

    while (i < len(tableau)):
        if(maxi < tableau[i][2]):
            maxi = tableau[i][2]
        i = i+1
        

    return maxi


## Affichage du Mininmum


def Minimum():

    mini = tableau[0][2]
    i=1

    while (i < len(tableau)):
        if(mini > tableau[i][2]):
            mini = tableau[i][2]
        i = i+1
        

    return mini


## Rechercher une valeur pour une date precise



## Calcul de la mayenne de poul dans une plage de temps

