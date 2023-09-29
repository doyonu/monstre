#Ulysse Doyon

import random

niveau_vie = 20
force_adversaire = random.randint(1,5)

print("bienvenue sur le meilleur jeu de l'univers !!! ")
print("Vous tombez face à face avec un adversaire de difficulté :%d"%(force_adversaire))
choix = int(input("Que voulez-vous faire ? " 
	"\n1- Combattre cet adversaire"
	"\n2- Contourner cet adversaire et aller ouvrir une autre porte"
	"\n3- Afficher les règles du jeu"
	"\n4- Quitter la partie"))