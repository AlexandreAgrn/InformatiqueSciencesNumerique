# Created by AUGRAIN Alexandre, RODRIGUE Andréa and PAREIRA Nicolas
# BAC 2016 - Spécialité ISN

from sys import stdin


# Fonction pour rechercher le fichier

def search(filename):
	# Ouvre le fichier en lecture
	fp=open(filename,"r")
	# Input le mot recherche
	sword=input("Entrez le mot à  rechercher.\n")
	# Initialisation
	ans=0
	# On lit le fichier lignes par lignes
	for line in fp.readlines():
		# On compte le nombre d'apparition(s) du mot voulu
		ans=ans+line.count(sword)
	# On ferme le fichier et affiche la réponse sous forme de liste
	fp.close()
	return [sword,ans]


# Fonction de remplacement de mot

def replace(filename):
	# Ouvre en lecture
	fp=open(filename,"r")
	# Input le mot que l'on veut remplacer
	oword=input("Entrez le mot à remplacer.\n")
	# Input le mot par lequel le remplacer
	nword=input("Entrez le nouveau mot.\n")
	# On parcourt le texte
	s=fp.read()
	# On ferme le fichier
	fp.close()
	# On remplace le nombre de fois
	s=s.replace(oword,nword)
	# On ouvre en mode écriture du fichier
	fp=open(filename,"w")
	# On ecrit la chaine de caractère dans le fichier
	fp.write(s)
	# On ferme le fichier
	fp.close()


# Fonction pour calculer le pourcentage d'apparition d'un mot

def cal_percentage(filename):
	# On ouvre le fichier en mode lecture
	fp=open(filename,"r")
	# On entre le mot pour lequel on calcule son pourcentage d'apparition
	pword=input("Entrez le mot pour lequel on calcul son pourcentage de présence.\n")
	# On lit le fichier en entier
	s=fp.read()
	# On ferme le fichier
	fp.close()
	# On compte les apparitions du mot
	occur=s.count(pword)
	# On calcule le nombre d'apparition global
	occur=occur*len(pword)
	# On calcule le nombre total de mots
	totwords=len(s)
	# On calcule le pourcentage final en multipliant par 1.0 afin d'avoir la précision du "float" (nombre à virgule)
	ans=(occur)/(totwords*1.0)*100
	return [pword,ans]


# Fonction pour coder en L33T

source=" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
code=" *•(o3|~#°☺♥1♪♠↕}$♣‼7!☻^▲?&*•(o3|~#°☺♥1♪♠↕}$♣‼7!☻^▲?&wihgfedcba"

def permute(message, origine, cryptage):
    traduction=""
    for i in range(len(message)):
        car = message[i]
        indice = 0
        trouve = False
        j=0
        while indice < len(origine) and not trouve:
            if car == origine[j]:
                trouve = True
                traduction = traduction + cryptage[j]
            j = j+1
        if not trouve :
            print("Caractère",car,"non trouvé dans la source")
    return traduction

# Input le nom du fichier à analyser
filename=input("Veuillez entrer le fichier (avec son extension .txt) à  analyser.\n")

# On affiche la liste d'options disponible pour l'utilisateur
options="[1] Rechercher un certain mot dans le fichier.\n[2] Remplacer un mot spécifique par un autre.\n[3] Calculer le pourcentage d'apparîtion d'un mot.\n[4] Coder un mot/une phrase en L33T\n[5] Quitter\n"

# Input des options
option=input(options)

# On continue de faire tourner le programme tant que l'utilisateur ne le quitte pas

while option!="5":
    if option=="1":
        k=search(filename)
        if k[1]==0:
            print("Le mot {0} n'a pas été trouvé.".format(k[0]))
        else:
            print("Le mot {0} apparaît {1} fois".format(k[0],k[1]))

    elif option=="2":
        replace(filename)
        print("Le(s) mot(s) a(ont) été remplacé(s) par le nouveau mot")

    elif option=="3":
        percen=cal_percentage(filename)
        print("Le mot {0} apparaît à  {1} pourcent(s)".format(percen[0],percen[1]))

    elif option=="4":
        alphabet=input("Le message à coder")
        permute(alphabet, source, code)
        resultat = permute(alphabet, source, code)
        reresultat = permute(resultat, code, source)
        print("Voilà, votre  ton message codé en L33T!")
        print(resultat)
        print(reresultat)

    else:
        print("Entrée invalide")

option=input(options)