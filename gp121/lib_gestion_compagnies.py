#--*-- coding:utf-8 --*--

from lib_commun import  ouverture_csv, ecriture_csv,realisAffichage

def affichage_compagnie(fname_compagnie) :
    """
    Cette procédure a pour objectif d'afficher l'ensemble des informations administratives des compagnies.
    Soit : nomComp,codOACI,siegeSocial,alliance,nbAvions,nbDessertes
    IN : le nom du fichier "descriptif_compagnies.txt" en entrée
    OUT : aucun retour
    """
    ##################################################
    #ouverture et recuperation du contenu du fichier
    ##################################################

    L_compagnies,entete = ouverture_csv(fname_compagnie)

    L_compagniesTries = []
    L_compagniesTries=sorted(L_compagnies, key=lambda x: x[0])
    
    nomColonnes = entete.split(",")
    nomColonnes[-1] = nomColonnes[-1][0:-1]  # on enleve \n
    nomTableau = "Description administrative des compagnies"
    
    realisAffichage(L_compagniesTries,nomTableau,nomColonnes)   


def ajout_compagnie(*admin_comp):
    """
    Cette procédure a pour objectif l'ajout des données administratives d'une nouvelle compagnie
    dans le fichier "descriptif_compagnies.txt"
    IN : sous forme du tuple admin_comp contenant nomComp,CodOACI,siegeSocial,alliance,nbAvions,nbDessertes,nom_Fichier
    OUT : appel à la fonction ecriture_csv pour insertion du nouveau contenu de fichier
	#----------------------------------------------------------------------------------------------- 
	comp_admin = une liste de chaines de caractères. Chaque chaine représente une compagnie aérienne
          format : nom_compagnie,code OACI,aeroport_principal,nom_alliance,nb_avions,nbDessertes,fname_compagnie
    """
    ##################################################
    #ouverture et recuperation du contenu du fichier
    ##################################################
    comp_admin,entete = ouverture_csv(admin_comp[-1])
    trouve = False
	#---------------------------------------------------------------------------------------
    # Vérification si la compagnie existe déjà dans le fichier "compagnies.txt"
	# Si la compagnie existe deja, on arrete le traitement et on prévient l operateur
    #---------------------------------------------------------------------------------------
    for ligne in comp_admin:
        if ligne[1] == admin_comp[1]:  # Comparaison basée sur le code OACI
            trouve = True
            break

    if trouve:
        print(f"La compagnie {admin_comp[0]} avec le code OACI {admin_comp[1]} existe déjà.")
        return
    
    #creation ss list
    nouvelle_compagnie = list(admin_comp[:-1])

    # Insertion en fin de liste de la sous-liste descriptive de la nouvelle compagnie
    comp_admin.append(nouvelle_compagnie)

    # Écriture dans le fichier
    ecriture_csv(comp_admin, admin_comp[-1], entete)


def maj_compagnie(*admin_comp):
    """
    Cette procédure a pour objectif d'actualiser le nombre d'avions ou de liaisons d'une compagnie
    dans le fichier "descriptif_compagnies.txt"
    IN : le nom de la compagnie, le nom du fichier "descriptif_compagnies.txt"
    OUT : néant
    #-----------------------------------------------------------------------------------------------    
    comp_admin = une liste de chaînes de caractères. Chaque chaîne représente une compagnie aérienne
          format : nom_compagnie, code OACI, aeroport_principal, nom_alliance, nb_avions, nb_liaisons
    """
    ##################################################
    #ouverture et récupération du contenu du fichier
    ##################################################
    comp_admin, entete = ouverture_csv(admin_comp[-1])
    
    #---------------------------------------------------------------------------------------
    # Vérification si la compagnie existe déjà dans le fichier "compagnies.txt" et sauvegarde
    # du rang ou on l'a trouvée dans comp_admin
    # Si la compagnie n'existe pas, on arrête le traitement et on prévient l'opérateur
    #---------------------------------------------------------------------------------------
    trouve = False
    rang = 0

    for i, ligne in enumerate(comp_admin):
        if ligne[0] == admin_comp[0]:
            trouve = True
            rang = i
            break

    if not trouve:
        print(f"La compagnie {admin_comp[0]} n'existe pas dans le fichier.")
        return

    # maj de l'enregistrement 
    print("Que voulez-vous modifier : \n1 - le nombre d'avions\n2 - le nombre de destinations")
    choix = int(input("Saisissez 1, 2\n==>"))

    if choix == 1:
        new_nb_avions = input("Entrez le nouveau nombre d'avions : ")
        comp_admin[rang][4] = new_nb_avions
    elif choix == 2:
        new_nb_liaisons = input("Entrez le nouveau nombre de liaisons : ")
        comp_admin[rang][5] = new_nb_liaisons
    else:
        print("Choix invalide.")
        return

    # Écriture 
    ecriture_csv(comp_admin, admin_comp[-1], entete)

def supprimer_compagnie(*supComp):
    """
    Cette fonction a pour objectif de supprimer une compagnie aérienne du fichier descriptif_compagnies.txt et du fichier composition_flotte.txt
    IN : supComp = (nomComp, fname_compagnie, fname_flotte)
    OUT : neant
    -----------------------------------------------------------------------------------------------
    comp_admin = une liste de chaines de caractères. Chaque chaine représente une compagnie aérienne
    format : nom_compagnie,code OACI,aeroport_principal,nom_alliance,nb_avions,nb_liaisons
    """

    ##################################################
    #ouverture et recuperation du contenu du fichier
    ##################################################
    comp_admin, enteteC = ouverture_csv(supComp[-2])
    flotte_comp, entete = ouverture_csv(supComp[-1])
    
    trouve = False
    rang = 0

    # Verification si la compagnie dispose encore d'un type avion dans le fichier composition_flotte.
    # Si c'est le cas, le traitement doit être interrompu et l'operateur prevenu
    for avion in flotte_comp:
        if avion[0] == supComp[0]:
            print(f"La compagnie {supComp[0]} dispose encore d'un type d'avion dans le fichier flotte. Suppression interrompue.")
            return
    
    # Recherche de la compagnie dans le fichier descriptif_compagnies
    for i, compagnie in enumerate(comp_admin):
        if compagnie[0] == supComp[0]:
            trouve = True
            rang = i
            break

    if trouve:
        # Suppression de la compagnie dans comp_admin
        comp_admin.pop(rang)
        print(f"La compagnie {supComp[0]} a été supprimée du fichier descriptif_compagnies.")
    else:
        print(f"La compagnie {supComp[0]} n'a pas été trouvée dans le fichier descriptif_compagnies.")
    
    ecriture_csv(comp_admin, supComp[-2], enteteC)
    print("Mise à jour du fichier descriptif_compagnies terminée.")