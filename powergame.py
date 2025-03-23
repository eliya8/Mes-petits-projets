from random import *
print("Bienvenue dans le jeu de pari sportif POWERGAME !")
nom = input("Entrez votre nom de joueur :")
gain = 0
print("Vous avez 0 dollars au début du jeu")
game = True 
club = ["Réal Madrid ","Bayern Munich ","FC Barcelone ","Liverpool ","Paris SG","Borussia Dortmund ","Bayer Leverkusen ","Lyon FC","Atletico Madrid ","AC Milan","Inter Milan","Chelsea FC","Manchester City","Manchester United ","Leeds FC","Arsenal FC","Tottenham FC","Lille FC","Benfica Lisbonne","Porto FC","Villarreal FC","Juventus Turin ","Rennes FC","Francfort FC","Schalk FC","Leipzig FC" ]

game = True
while game :
	club1 = choice(club)
	club2 = choice(club)
	if club1 == club2:
	     club1 = choice(club)
	     club2 = choice(club)
	     
	score1 = randrange(5)
	score2 = randrange(5)
	print("Hello, le match opposera les clubs",club1,"et",club2)
	n = 6
	while n == 6:
		print("Prédis le score",club1)
		p1 = input()
		try :
			p1 = int(p1)
		except ValueError :
			print("Valeur incorrecte. Veuillez prédire un chiffre exacte")
		else :
			n = 7
			
	x = 5
	while x == 5 :
		print("Prédis le score ",club2)
		p2 = input()
		try :
			p2 = int(p2)
		except ValueError :
			print("Valeur incorrecte. Veuillez prédire un chiffre exacte")
		else :
			x = 0
			
	if p1 == score1 and p2 == score2 :
			print("Bien joué l'ami ! Le match a bel et bien eu un score final de",club1,score1, "-",score2,club2)
			gain += 1000
			print("Tu gagnes 1000$ . Cool !!")
	else :
		print("Malheureusement,tu as perdu. Le match a eu un score final de",club1,score1, "-",score2,club2)
		
	c = input("Tapez Q pour quitter :")
	c = str(c)
	if c == "Q" :
		print("Au revoir",nom,". Tu quittes le jeu avec",gain,"$. À plus")
		game = False