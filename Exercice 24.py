#Exercice24
#Ecrire un programme qui permet de trouver le maximum et le minimum des elements d'une matrice
matrice=[
    [4, 7, 6],
    [13, 8, 9],
    [3, 15,42]
    ]
minimum=min(min(ligne) for ligne in matrice)
maximum=max(max(ligne) for ligne in matrice)
print("le minimum est :", minimum)
print("le maximum est :", maximum)
