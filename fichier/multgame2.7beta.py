version = str("Bêta 2.7")
##### Notions #####
'''
Ligne ;
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
General ;
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    print(f"{bcolors.jaune}Multgame.py \nCréer par Thedrewen#8306 \nVersion : ", version)
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    sleep(1)
    print(f"{bcolors.gras}Message systéme : ", msg_sys,f"{bcolors.fin}")
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")

Fin ;
    sleep(2)
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    msg_sys = str("Aucun message systéme")
    print(f"{bcolors.jaune}Chargements...")
    sleep(1)
'''


##### Importations #####
from random import *
from time import *
from pickle import *
import os


##### Class #####

# class couleurs
class bcolors:
    mauve = '\033[95m' #Mauve flash
    bleu = '\033[94m' #bleu
    cyan = '\033[96m' #Cyan
    vert = '\033[92m' #vert
    jaune = '\033[93m' #jaune
    rouge = '\033[91m' #rouge
    fin = '\033[0m' #couleurs base
    gras = '\033[1m' #gras
    ligne = '\033[4m' #ligne


##### Introduction #####
print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
print(f"{bcolors.jaune}Multgame.py \nCréer par Thedrewen#8306 \nVersion :", version)
print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
sleep(1)
print(f"{bcolors.rouge}\nImportations des modules requis...")
sleep(3)
os.system("clear")

##### Fonctions de paramétrage #####
def start():
    global nj
    global msg_sys
    global score_j
    global score_j2
    global score_j3
    global score_j4
    global player_name
    global player_name2
    global player_name3
    global player_name4
    global data
    os.system("clear")
    sleep(1)
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    print(f"{bcolors.jaune}Multgame.py \nCréer par Thedrewen#8306 \nVersion : ", version)
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    sleep(1)
    print(f"{bcolors.gras}Message systéme : ", msg_sys,f"{bcolors.fin}")
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")

    print(f"{bcolors.cyan}{bcolors.gras}Nom et score :{bcolors.fin}")
    print(f"{bcolors.jaune}",player_name, " : ", score_j)
    if int(nj) >= 2:
        print(f"{bcolors.jaune}",player_name2, " : ", score_j2)
        if int(nj) >= 3:
            print(f"{bcolors.jaune}",player_name3, " : ", score_j3)
            if int(nj) == 4:
                print(f"{bcolors.jaune}",player_name4, " : ", score_j4)
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")

    print(f"{bcolors.cyan}{bcolors.gras}Commandes :{bcolors.fin}")
    print(f"{bcolors.rouge}Quitter : q\nParamétre : p\n{bcolors.vert}Le juste nombre : 1\nPierre Feuille Siceaux : 2\nLe jeux de Nol_Ice : 3{bcolors.fin}")
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    choix = str(input(f"{bcolors.mauve}Choisisez la fonction à lancer : {bcolors.fin}"))
    msg_sys = str("Aucun message systéme")

    if choix == str("q"):
        os.system("clear")
        quit
    elif choix == str("p"):
        config()
    elif choix == str("1"):
        j1()
    elif choix == str("2"):
        j2()
    elif choix == str("3"):
        j3()
    else:
        msg_sys = str("Erreur de syntaxe !")
        start()


def config():
    global msg_sys
    sleep(1)
    os.system("clear")
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    print(f"{bcolors.jaune}Multgame.py \nCréer par Thedrewen#8306 \nVersion : ", version)
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    sleep(1)
    print(f"{bcolors.gras}Message systéme : ", msg_sys,f"{bcolors.fin}")
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    print(f"{bcolors.cyan}{bcolors.gras}Commandes :{bcolors.fin}")
    print(f"{bcolors.rouge}Retour : b\nRéinisialiser : r\nJoueurs : j\nSauvegarder : s\nCharger : c{bcolors.fin}")
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    choix = str(input(f"{bcolors.mauve}Choisisez la fonction à lancer : {bcolors.fin}"))
    msg_sys = str("Aucun message systéme")

    if choix == str("b"):
        start()
    elif choix == str("r"):
        reset()
    elif choix == str("j"):
        joueurs()
    elif choix == str("s"):
        save()
    elif choix == str("c"):
        charger()
    else:
        msg_sys = str("Erreur de syntaxe !")
        config()


def reset():
    global nj
    global msg_sys
    global score_j
    global score_j2
    global score_j3
    global score_j4
    global player_name
    global player_name2
    global player_name3
    global player_name4
    os.system("clear")
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    print(f"{bcolors.jaune}Multgame.py \nCréer par Thedrewen#8306 \nVersion : ", version)
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    sleep(1)
    print(f"{bcolors.gras}Message systéme : ", msg_sys,f"{bcolors.fin}")
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    print(f"{bcolors.rouge}\n Réinisialisation en cours...\n{bcolors.fin}")
    nj = 1
    msg_sys = str("Réinisialisation completer !")
    score_j = int(0)
    score_j2 = int(0)
    score_j3 = int(0)
    score_j4 = int(0)
    sleep(3)
    start()


def joueurs():
    global nj
    global msg_sys
    global score_j
    global score_j2
    global score_j3
    global score_j4
    global player_name
    global player_name2
    global player_name3
    global player_name4
    os.system("clear")
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    print(f"{bcolors.jaune}Multgame.py \nCréer par Thedrewen#8306 \nVersion : ", version)
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    sleep(1)
    print(f"{bcolors.gras}Message systéme : ", msg_sys,f"{bcolors.fin}")
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    nj = int(input(f"{bcolors.mauve}Quel est le nombre de joueurs (1-4) : {bcolors.fin}"))
    sleep(1)
    player_name = str(input(f"{bcolors.mauve}Pseudo du joueur 1?{bcolors.fin} "))
    if nj >= 2:
        player_name2 = str(input(f"{bcolors.mauve}Pseudo du joueur 2?{bcolors.fin} "))
        if nj >= 3:
            player_name3 = str(input(f"{bcolors.mauve}Pseudo du joueur 3?{bcolors.fin} "))
            if nj == 4:
                player_name4 = str(input(f"{bcolors.mauve}Pseudo du joueur 4?{bcolors.fin} "))
    msg_sys = str('La fonction "joueurs" a bien été configurer !')
    start()


def save():
    global file
    global msg_sys
    global nj
    global score_j
    global score_j2
    global score_j3
    global score_j4
    global player_name
    global player_name2
    global player_name3
    global player_name4
    os.system("clear")
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    print(f"{bcolors.jaune}Multgame.py \nCréer par Thedrewen#8306 \nVersion : ", version)
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    sleep(1)
    print(f"{bcolors.gras}Message systéme : ", msg_sys,f"{bcolors.fin}")
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    save_name = str(input(f"{bcolors.mauve}\nSi vous-nommez la souvegarde avec un nom déjà présent, celui-ci ecrasera l'ancien !\nQuel nom donnez vous à cette sauvegarde : {bcolors.fin}"))
    if not os.path.exists("save"):
        os.mkdir("save")
    file = open("save/"+save_name,"wb")
    dump(nj, file)
    dump(score_j, file)
    dump(score_j2, file)
    dump(score_j3, file)
    dump(score_j4, file)
    dump(player_name, file)
    dump(player_name2, file)
    dump(player_name3, file)
    dump(player_name4, file)
    msg_sys = str("Sauvegarder avec succés !")
    file.close()
    start()


def charger():
    global file
    global msg_sys
    global nj
    global score_j
    global score_j2
    global score_j3
    global score_j4
    global player_name
    global player_name2
    global player_name3
    global player_name4
    if not os.path.exists("save"):
        os.makedirs("save")
    os.system("clear")
    list = os.listdir("save/")
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    print(f"{bcolors.jaune}Multgame.py \nCréer par Thedrewen#8306 \nVersion : ", version)
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    sleep(1)
    print(f"{bcolors.gras}Message systéme : ", msg_sys,f"{bcolors.fin}")
    print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
    print(f"{bcolors.mauve}\nListe des sauvegardes : \n",list)
    save_name = str(input(f"Quel sauvegarde voulez-vous charger : {bcolors.fin}"))
    msg_sys = str('Sauvegarde chargée avec succés !')
    try:
        file = open("save/"+save_name, "rb")
        nj = load(file)
        score_j = load(file)
        score_j2 = load(file)
        score_j3 = load(file)
        score_j4 = load(file)
        player_name = load(file)
        player_name2 = load(file)
        player_name3 = load(file)
        player_name4 = load(file)
        file.close()
        msg_sys = str("Sauvegarde chargée avec succés !")
    except:
        msg_sys = str("Aucune sauvegarde trouvée.")
    start()


##### Jeux #####
# Le juste nombre
def j1():
    global nj
    global msg_sys
    global score_j
    global score_j2
    global score_j3
    global score_j4
    global player_name
    global player_name2
    global player_name3
    global player_name4
    joueur_pfc = 0
    for i in range(int(nj)):
        #system multi
        os.system("clear")
        joueur_pfc += 1
        if joueur_pfc == 1:
            msg_sys = str("à "+str(player_name)+" de jouer !")
        elif joueur_pfc == 2:
            msg_sys = str("à "+str(player_name2)+" de jouer !")
        elif joueur_pfc == 3:
            msg_sys = str("à "+str(player_name3)+" de jouer !")
        elif joueur_pfc == 4:
            msg_sys = str("à "+str(player_name4)+" de jouer !")
        #system random
        sleep(2)
        os.system("clear")
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        print(f"{bcolors.jaune}Multgame.py \nCréer par Thedrewen#8306 \nVersion : ", version)
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        sleep(1)
        print(f"{bcolors.gras}Message systéme : ", msg_sys,f"{bcolors.fin}")
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        rnd = int(randint(0, 100))
        n = int(input(f"{bcolors.cyan}Quel est le nombre entre 0 et 100 ? {bcolors.fin}"))
        test = 1
    
        while rnd != n:
            if n < rnd:
                print(f"{bcolors.rouge}Plus Grand !")
                n = int(input(f"{bcolors.cyan}Quel est le nombre entre 0 et 100 ? "))
                test = test + 1
            else:
                print(f"{bcolors.rouge}Plus Petit !")
                n = int(input(f"{bcolors.cyan}Quel est le nombre entre 0 et 100 ? "))
                test = test + 1
                    
        os.system("clear")
        sleep(2)
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        print(f"{bcolors.jaune}Multgame.py \nCréer par Thedrewen#8306 \nVersion : ", version)
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        sleep(1)
        print(f"{bcolors.gras}Message systéme : ", msg_sys,f"{bcolors.fin}")
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        print(f"{bcolors.vert}Bien jouer ! Tu as trouver : "+str(rnd))
        print("Avec "+str(test)+" Tentative(s).")
        #Systeme Points
        if test >= 19 and test <= 20:
            if joueur_pfc == 1:
                score_j += 1
            elif joueur_pfc == 2:
                score_j2 += 1
            elif joueur_pfc == 3:
                score_j3 += 1
            elif joueur_pfc == 4:
                score_j4 += 1
        elif test >= 17 and test <= 18:
            if joueur_pfc == 1:
                score_j += 2
            elif joueur_pfc == 2:
                score_j2 += 2
            elif joueur_pfc == 3:
                score_j3 += 2
            elif joueur_pfc == 4:
                score_j4 += 2
        elif test >= 15 and test <= 16:
            if joueur_pfc == 1:
                score_j += 3
            elif joueur_pfc == 2:
                score_j2 += 3
            elif joueur_pfc == 3:
                score_j3 += 3
            elif joueur_pfc == 4:
                score_j4 += 3
        elif test >= 13 and test <= 14:
            if joueur_pfc == 1:
                score_j += 4
            elif joueur_pfc == 2:
                score_j2 += 4
            elif joueur_pfc == 3:
                score_j3 += 4
            elif joueur_pfc == 4:
                score_j4 += 4
        elif test >= 11 and test <= 12:
            if joueur_pfc == 1:
                score_j += 5
            elif joueur_pfc == 2:
                score_j2 += 5
            elif joueur_pfc == 3:
                score_j3 += 5
            elif joueur_pfc == 4:
                score_j4 += 5
        elif test >= 9 and test <= 10:
            if joueur_pfc == 1:
                score_j += 6
            elif joueur_pfc == 2:
                score_j2 += 6
            elif joueur_pfc == 3:
                score_j3 += 6
            elif joueur_pfc == 4:
                score_j4 += 6
        elif test >= 7 and test <= 8:
            if joueur_pfc == 1:
                score_j += 7
            elif joueur_pfc == 2:
                score_j2 += 7
            elif joueur_pfc == 3:
                score_j3 += 7
            elif joueur_pfc == 4:
                score_j4 += 7
        elif test >= 5 and test <= 6:
            if joueur_pfc == 1:
                score_j += 8
            elif joueur_pfc == 2:
                score_j2 += 8
            elif joueur_pfc == 3:
                score_j3 += 8
            elif joueur_pfc == 4:
                score_j4 += 8
        elif test >= 3 and test <= 4:
            if joueur_pfc == 1:
                score_j += 9
            elif joueur_pfc == 2:
                score_j2 += 9
            elif joueur_pfc == 3:
                score_j3 += 9
            elif joueur_pfc == 4:
                score_j4 += 9
        elif test >= 1 and test <= 2:
            if joueur_pfc == 1:
                score_j += 10
            elif joueur_pfc == 2:
                score_j2 += 10
            elif joueur_pfc == 3:
                score_j3 += 10
            elif joueur_pfc == 4:
                score_j4 += 10
        sleep(1)
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        msg_sys = str("Aucun message systéme")
        print(f"{bcolors.jaune}Chargements...")
        sleep(2)
    sleep(1)
    start()

# pfc
def j2():
    global nj
    global msg_sys
    global score_j
    global score_j2
    global score_j3
    global score_j4
    global player_name
    global player_name2
    global player_name3
    global player_name4
    joueur_pfc = 0
    for i in range(int(nj)):
        # Systeme aléatoire ordi
        list_el = ["p","f","c"]
        
        list_rnd = randint(0, 2)
        
        elements_ordi = list_el[list_rnd]
        
        if elements_ordi == "p":
            str_ordi = str("pierre")
        else:
            if elements_ordi == "f":
                str_ordi = str("feuille")
            else:
                str_ordi = str("ciseaux")

        #System multi
        os.system("clear")
        joueur_pfc = joueur_pfc + 1
        if joueur_pfc == 1:
            msg_sys = str("à "+str(player_name)+" de jouer !")
        elif joueur_pfc == 2:
            msg_sys = str("à "+str(player_name2)+" de jouer !")
        elif joueur_pfc == 3:
            msg_sys = str("à "+str(player_name3)+" de jouer !")
        elif joueur_pfc == 4:
            msg_sys = str("à "+str(player_name4)+" de jouer !")
        sleep(2)
        
        # Demande à l'utilisateur
        os.system("clear")
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        print(f"{bcolors.jaune}Multgame.py \nCréer par Thedrewen#8306 \nVersion : ", version)
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        sleep(1)
        print(f"{bcolors.gras}Message systéme : ", msg_sys,f"{bcolors.fin}")
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        print(f"{bcolors.vert}Pierre = p , Feuille = f , Ciseaux = c")
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        element_player = str(input(f"{bcolors.jaune}Quel éléments jouer vous ? {bcolors.fin}"))

        while not (element_player == str("p") or element_player == str("f") or element_player == str("c")):
            msg_sys = str("Erreur de syntaxe !")
            os.system("clear")
            print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
            print(f"{bcolors.jaune}Multgame.py \nCréer par Thedrewen#8306 \nVersion : ", version)
            print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
            sleep(1)
            print(f"{bcolors.gras}Message systéme : ", msg_sys,f"{bcolors.fin}")
            print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
            print(f"{bcolors.vert}Pierre = p , Feuille = f , Ciseaux = c")
            print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
            element_player = str(input(f"{bcolors.jaune}Quel éléments jouer vous ? "))


        print(f"{bcolors.mauve}Ordinateur : "+str(str_ordi))

        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")

        if elements_ordi == element_player:
            print(f"{bcolors.cyan}Egalité !{bcolors.fin}")
        else:
            if (elements_ordi == "p" and element_player == "c") or (elements_ordi == "f" and element_player == "p") or (elements_ordi == "c" and element_player == "f"):
                print(f"{bcolors.rouge}Vous avez perdue !")
            else:
                print(f"{bcolors.vert}Vous avez gagner !")
                if joueur_pfc == 1:
                    score_j += 1
                elif joueur_pfc == 2:
                    score_j2 += 1
                elif joueur_pfc == 3:
                    score_j3 += 1
                elif joueur_pfc == 4:
                    score_j4 += 1
        sleep(2)
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        msg_sys = str("Aucun message systéme")
        print(f"{bcolors.jaune}Chargements...")
        sleep(1)
    sleep(1)
    start()

def j3():
    global nj
    global msg_sys
    global score_j
    global score_j2
    global score_j3
    global score_j4
    global player_name
    global player_name2
    global player_name3
    global player_name4
    joueur_pfc = 0
    for i in range(int(nj)):
        os.system("clear")
        sleep(1)
        joueur_pfc += 1
        if joueur_pfc == 1:
            msg_sys = str("à "+str(player_name)+" de jouer !")
        elif joueur_pfc == 2:
            msg_sys = str("à "+str(player_name2)+" de jouer !")
        elif joueur_pfc == 3:
            msg_sys = str("à "+str(player_name3)+" de jouer !")
        elif joueur_pfc == 4:
            msg_sys = str("à "+str(player_name4)+" de jouer !")
        # Systeme aléatoire
        un = int(randint(1, 3))
        deux = int(randint(1, 3))
        trois = int(randint(1, 3))

        #print
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        print(f"{bcolors.jaune}Multgame.py \nCréer par Thedrewen#8306 \nVersion : ", version,f"\n{bcolors.mauve}Jeu créer par Nol_Ice#5088")
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        sleep(1)
        print(f"{bcolors.gras}Message systéme : ", msg_sys,f"{bcolors.fin}")
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        sleep(1)
        print(f"{bcolors.jaune}Le but du jeu et d'obtenir le nombre 1 dans les 3 variables.")
        sleep(3)
        print("1) ", un)
        sleep(1)
        print("2) ", deux)
        sleep(1)
        print("3) ", trois)
        sleep(2)
        os.system("clear")
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        print(f"{bcolors.jaune}Multgame.py \nCréer par Thedrewen#8306 \nVersion : ", version,f"\n{bcolors.mauve}Jeu créer par Nol_Ice#5088")
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        sleep(1)
        print(f"{bcolors.gras}Message systéme : ", msg_sys,f"{bcolors.fin}")
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        #if
        sleep(2)
        if un == 1 and deux == 1 and trois == 1:
            print(f"{bcolors.vert}Vous avez gagner et vous remportez 5 point.")
            if nj == 1:
                score_j += 5
            elif nj == 2:
                score_j2 += 5
            elif nj == 3:
                score_j3 += 5
            else:
                score_j4 += 5
        else:
            print(f"{bcolors.rouge}Vous avez perdue.{bcolors.fin}")
        sleep(2)
        print(f"{bcolors.bleu}{bcolors.ligne}                              {bcolors.fin}")
        msg_sys = str("Aucun message systéme")
        print(f"{bcolors.jaune}Chargements...")
        sleep(1)
    sleep(1)
    start()


##### Lancements #####

# Variables de base
nj = 1
msg_sys = str("Aucun message systéme")
score_j = int(0)
score_j2 = int(0)
score_j3 = int(0)
score_j4 = int(0)
player_name = str("Inconnue")
player_name2 = str("Inconnue")
player_name3 = str("Inconnue")
player_name4 = str("Inconnue")

# Start
os.system("clear")
start()
