#--*-- coding:utf8 --*--
#-------------------------------------------------------------------------------
# Name:        Gestion répertoire téléphonique
# Purpose:
#
# Author:      vquet
#
# Created:     26/12/2016
# Copyright:   (c) vquet 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#from lib_commun import  ouverture_csv, ecriture_csv,realisAffichage
from lib_gestion_compagnies import affichage_compagnie,ajout_compagnie,maj_compagnie,supprimer_compagnie
from lib_gestion_flottes import affichage_flotte,ajout_maj_type_avion_compagnie,supprimer_type_avion_compagnie

fname_compagnie = "descriptif_compagnies.txt"
fname_flotte = "compositions_flottes_v2.txt"



#***************************************************************************
#---------------------------------------------------------------------------
#                  Programme principal
#---------------------------------------------------------------------------
#***************************************************************************

#fname_compagnie = "descriptif_compagnies.txt"
#fname_flotte = "compositions_flottes_v2.csv"

menu_choix = 0

while True:
    menu_choix = int(input("Rentrez votre choix ( valeur entre 1-7): \n 1- Affichage compagnies \n 2- Affichage parc_avion par compagnie\n 3- Ajout compagnie\n 4- M-a-J compagnie\n 5- ajout_mofid_type-qte_avion_compagnie\n 6- Supprimer type avion compagnie\n 7- Supprimer une compagnie\n 8- Sortie\n==> "))
    if menu_choix == 1:
        affichage_compagnie(fname_compagnie)
        
    elif menu_choix == 2:
        affichage_flotte(fname_flotte)

    elif menu_choix == 3:
        print("Choix 3. Ajouter compagnie aerienne (nom, code,siegeSocial, alliance,nbAv et nbDessertes)")
        nomComp = input("Nom compagnie (ex : air_france) : ")
        CodOACI = input("Code AOCI : ")
        siegeSocial = input("Siege social : ")
        alliance = input("Alliance :")
        nbAvions = input("Nombre avions :")
        nbDessertes = input("Nombre dessertes :")
        ajout_compagnie(nomComp,CodOACI,siegeSocial,alliance,nbAvions,nbDessertes,fname_compagnie)

    elif menu_choix == 4:
        print("Choix 4. Mise à jour d une compagnie")
        nomComp = input("Nom compagnie (ex : air_france) \n==>")
        maj_compagnie(nomComp,fname_compagnie)


    elif menu_choix == 5:
        print("Choix 5. Ajouter type avion et/ou qte pour une compagnie\nSi le type existe deja, on ajoute ou supprime\nune quantite dans le type\n")
        nomComp = input("Nom compagnie (ex : air_france)\n==>  ")
        typeAvion = input("Type de l'avion (ex : A350, , B787\n==>  ")
        qte = input("Quantite ajoutee ou supprimee dans le type\n==>  ")
        ajout_maj_type_avion_compagnie(nomComp, typeAvion, qte,fname_compagnie,fname_flotte)


    elif menu_choix == 6:
        print("Choix 6. Supprimer un type avion d'une compagnie\n==>  ")
        nomComp = input("Nom compagnie (ex : air_france) : \n==>  ")
        typeAvion = input("Type de l'avion (ex : A350, , B787\n==>  ")
        supprimer_type_avion_compagnie(nomComp, typeAvion,fname_compagnie,fname_flotte)

    elif menu_choix == 7:
        print("Choix 7. supprimer une compagnie (ex : air_france) :")
        nomComp = input("Nom compagnie (ex : air_france) : ")
        supprimer_compagnie(nomComp,fname_compagnie,fname_flotte)

    elif menu_choix == 8:
        print("Choix 8. Quitter")
        break

print("Au revoir")