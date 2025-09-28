def menu(*args):
    """ cette fonction permet de gérer un menu utilisateur
    entrer toutes les fonctions d'un code"""
    
    #verifie que les arguments donner ne sont pas nul
    if len(args) == 0:
        print("\033[1;31m /!\\ you must call at least one function in menu() /!\\ \033[1;31m")
        return
    
    # permet d'afficher le premier choix
    print("0 - STOP")
    # affiche les autres choix dynamiquement
    for i, func in enumerate(args):
        print(i+ 1, "-", func.__name__)

    # boucle infini
    while True:
        #gere les choix
        choix = input()
        if choix == str(0):
            break
        try:
            args[(int(choix)- 1)]()
        #erreur de valeur exemple un caractere au lieu d'un chiffre
        except ValueError:
            choix = input("entrer un chiffre correct")
        # erreur d'index si le chiffre donner est trop grand
        except IndexError:
            choix = input("entrer un chiffre correct")
