#--*-- coding:utf-8 --*--
import os

def ouverture_csv(nomfichier):
    """
    Cette fonction a pour objectif l'ouverture d'un fichier au format texte
    IN : le nom du fichier à traiter
    OUT : - fic_input = une liste de listes de chaines de caractères. Chaque sous-liste représente une enregistrement du fichier Descriptif_compagnies.txt 
                     ex : air_france,AFR,charles_de_gaulle,skyteam,333,210
          - entete = une chaine de caractères contenant le nom des colonnes du fichier ex pour le  fichier Descriptif_compagnies.txt : nomComp,codOACI,siegeSocial,alliance,nbAvions,nbDessertes
    """
    import os
    ##################################################
    #ouverture et recuperation du contenu du fichier
    ##################################################

    print("nomfichier = ",nomfichier)
    fic_input = []

    zone_Echange = open(nomfichier, 'r')


    entete = zone_Echange.readline()


    for ligne in zone_Echange.readlines():
        pt_data = ligne.split(sep=',')
        fic_input.append(pt_data)

    zone_Echange.close()
    return  fic_input,entete


def ecriture_csv(contenu_fichier, nomFichier, entete):
    """
    Cette fonction a pour objectif l'ecriture du resultat d'un traitement dans un fichier txt
    IN : une liste de listes de chaines de caractères, le nom du fichier à traiter et le nom des entetes de colonne du fichier
    OUT : néant
    """
    ##################################################
    # ouverture et recuperation du contenu du fichier
    ##################################################

    fic_output = []
    fic_output.append(entete + '\n')

    for ligne in contenu_fichier:
        fic_output.append(','.join(ligne) + '\n')

    with open(nomFichier, 'w') as zone_Echange:
        zone_Echange.writelines(fic_output)






def realisAffichage(L_affichage,nomTableau,nomColonnes):
    """
    Cette fonction a pour objectif d afficher le contenu des fichiers descriptif_compagnies.txt ou compositions_flottes_v2.txt 
    IN : le contenu du fichier a afficher sous forme d une liste de listes de chaines de caractères, le nom du tableau a faire apparaitre et le nom des colonnes du tableau
    OUT : un affichage conforme
    """
    ##################################################
    #ouverture et recuperation du contenu du fichier
    ##################################################

    #---------------------------------
    # preparation Affichage
    #---------------------------------

    longDonRef = [0 for i in range(len(nomColonnes))]  # initialisation de la reference longueur max des donnees par colonne

    for i in range(0,len(L_affichage)) :
        L_affichage[i][-1] = (L_affichage[i][-1][0:-1]) # on enleve le \n de fin de ligne

    # on recherche la longueur max d une donnee pour une colonne et on l a stocke dans longDonRef pour le rang considere


    # *******************   A COMPLETER   *******************************************
