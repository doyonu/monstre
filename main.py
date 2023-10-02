#Ulysse Doyon

import random

niveau_vie = 20
nombre_victoires_consecutives = 0
x = 1
numero_adversaire = 1
nombre_victoires = 0
nombre_defaites = 0
numero_combat = 0
force_adversaire = 1

print("bienvenue sur le MEILLEUR jeu de l'univers !!! ")
while x == 1:
	force_adversaire = random.randint(1,5)
	print("Vous tombez face à face avec un adversaire de difficulté :%d"%(force_adversaire))
	choix = int(input("Que voulez-vous faire ? " 
		"\n1- Combattre cet adversaire"
		"\n2- Contourner cet adversaire et aller ouvrir une autre porte"
		"\n3- Afficher les règles du jeu"
		"\n4- Quitter la partie\n"))
	if choix == 1:
		numero_combat += 1
		print("Adversaire :%d "
		"Force de l’adversaire :%d "
		"Niveau de vie de l’usager :%d "
		"Combat %d : %d / %d"%(numero_adversaire,force_adversaire,niveau_vie,
										   numero_combat,nombre_victoires,nombre_defaites))
		score_de = random.randint(1,6)
		print("Lancer du dé :%d"%(score_de))
		if score_de <= force_adversaire:
			niveau_vie = niveau_vie - force_adversaire
			print("vous perdez le combat\nNiveau de vie :%d"%(niveau_vie))
			if niveau_vie <= 0:
				print("La partie est terminée, vous avez vaincu %d monstre(s)."%(nombre_victoires))
				x = 0
		else:
			niveau_vie = niveau_vie + force_adversaire
			nombre_victoires_consecutives += 1
			print("vous gagnez le combat\nNiveau de vie :%d\nNombre de victoires consécutives :%d"%(niveau_vie,nombre_victoires_consecutives))

	elif choix == 2:
		print("vous perdez un point de vie")
		niveau_vie -= 1
	elif choix == 3:
		print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire."
		"Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire."
		"Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire."
		"Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n\n"
		"La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n\n"
		"L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")
	elif choix == 4:
		print("Merci et au revoir...")
		x = 0
	else:
		print("un misclick (surement)")