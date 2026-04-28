#Exercice16
#Un algorithme qui affiche l'inevrse d'un mot sans changé le mot
chaine=input("saisir votre mot: ")
if chaine==chaine[::-1]:
    print("La chaine est un Paliendrom")
else:
    print("La chaine n'est un Paliendrom")

