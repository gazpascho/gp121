#--*-- coding:utf-8 --*--

from lib_commun import  ouverture_csv, ecriture_csv,realisAffichage


def affichage_flotte(fname_flotte) :
    """
    Cette procédure a pour objectif d'afficher l'ensemble des informations administratives des compagnies.
    Soit : nomComp,codOACI,siegeSocial,alliance,nbAvions,nbDessertes
    IN : le nom du fichier "descriptif_compagnies.txt" en entrée
    OUT : aucun retour
    """
    ##################################################
    #ouverture et recuperation du contenu du fichier
    ##################################################

    L_flottes,entete = ouverture_csv(fname_flotte)

    L_flottesTries = []
    L_flottesTries=sorted(L_flottes, key=lambda x: x[0])
    
    nomColonnes = entete.split(",")
    nomColonnes[-1] = nomColonnes[-1][0:-1]  # on enleve \n
    nomTableau = "Composition de la flotte des compagnies"
    
    realisAffichage(L_flottesTries,nomTableau,nomColonnes)    


def ajout_maj_type_avion_compagnie(*new_type_comp ):
    """
    Cette fonction a pour objectif l'ajout ou la mise à jour d'un type d'avions ou de la quantité d'avions pour
        un type d'avion dans une compagnie dans le fichier compositions_flottes_v2.json
    IN : nom de la Compagnie, le type d'Avion, la quantité, le nom du fichier des compagnies et le nom du fichier des flottes avions
      (nomComp, typeAvion, qte,fname_compagnie,fname_flotte)
    OUT : neant
	#-----------------------------------------------------------------------------------------------	
	"""
    present = False # sera utilisée plus tard pour vérifier si une mise à jour doit être effectuée.
    ##################################################
    #ouverture et recuperation du contenu du fichier
    ##################################################

    print("new_type_comp[-1] = ",new_type_comp[-1])
    print("new_type_comp[-2] = ",new_type_comp[-2])

    comp_admin,enteteC = ouverture_csv(new_type_comp[-2])  #new_type_comp[-2] = "descriptif_compagnies.txt"
    flotte_comp,entete = ouverture_csv(new_type_comp[-1])  #new_type_comp[-1] = "compositions_flottes_v2.csv"

    #---------------------------------------------------------------------------------------
    # Vérification si la compagnie existe déjà dans le fichier "descriptif_compagnies.txt"
    #---------------------------------------------------------------------------------------

    # on met met present comme True a chaque qu'on trouve une compagnie qui existe déjà dans le fichier et on continue. Une fois qu'une difference est trouvée, on sort de la boucle 
    for nom_comp in comp_admin :
        if nom_comp[0]==new_type_comp[0] : #avec new type conf la liste avec les nouvelles infos a comparé avec nom_comp
            present = True
            continue
        else :
            present = False
            break 
    

    #---------------------------------------------------------------------------------------
    #  Si la compagnie n'existe pas dans le fichier "descriptif_compagnies.txt"
    # Il est indispensable de la créer
    #---------------------------------------------------------------------------------------


    if present==True :
        nouvelle_liste= new_type_comp[0] # On crée une nouvelle liste avec le nom de la compagnie
        comp_admin.append(nouvelle_liste) #On ajoute la nouvelle liste a comp_admin
    print("etape deux a marcher")
    
    # Analyse du signe de la réponse. Si le signe est absent, il faut refuser la réponse et prévenir
    rep=""
    new_flotte=""
    for i in range(len(flotte_comp)):
        
    # Vérifier si la compagnie est déjà dans la liste
        if flotte_comp[i][0] == new_flotte[0]:
        # Vérifier si le type d'avion correspond
            if flotte_comp[1] == new_flotte[1]:
            # Vérifier le signe de la réponse
                if rep[0] == '+':
                    flotte_comp[i][-1] = str(int(new_flotte[-1]) + int(rep[1:]))
                elif rep[0] == '-':
                # Vérifier si le nombre d'avions à retirer ne dépasse pas le nombre total
                    if int(new_flotte[-1]) >= int(rep[1:]):
                        flotte_comp[i][-1] = str(int(new_flotte[-1]) - int(rep[1:]))
                    else:
                        print("La réponse n'est pas correcte. Le nombre d'avions à retirer est supérieur au nombre total.")
                else:
                    print("La réponse n'est pas correcte. Le signe de l'opération est absent.")


    ####################################
    # Recuperation des valeurs saisies
    ####################################
    # new_type_comp = nomComp, typeAvion, qte
    # je cherche si le type d avion existe deja pour la compagnie
    trouve = False
    rang = 0


















    ################################################
    #  Ouverture fichier et ecriture nouveau contenu
    ################################################

    ecriture_csv(flotte_comp,new_type_comp[-1],entete)



def supprimer_type_avion_compagnie(*sup_type_comp):
    """
    Cette fonction a pour objectif la suppression d'un type d'avion pour une compagnie donnée
    IN : le tuple sup_type_comp contenant (nomComp, typeAvion, fname_compagnie, fname_flotte)
    OUT : néant
    """
    # Chargement des données
    comp_admin, enteteC = ouverture_csv(sup_type_comp[-2])
    flotte_comp, entete = ouverture_csv(sup_type_comp[-1])

    # Vérification de l'existence de la compagnie
    compagnie_existante = False
    for company in comp_admin:
        if company[0] == sup_type_comp[0]:
            compagnie_existante = True
            break

    if not compagnie_existante:
        print(f"Compagnie {sup_type_comp[0]} non trouvée dans le fichier {sup_type_comp[-2]}.")
        return

    # Suppression du type d'avion
    nouvelle_flotte = [avion for avion in flotte_comp if not (avion[0] == sup_type_comp[0] and avion[1] == sup_type_comp[1])]

    # Écriture du résultat dans le fichier
    ecriture_csv(nouvelle_flotte, sup_type_comp[-1], entete)
    return
