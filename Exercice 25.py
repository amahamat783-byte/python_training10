#Exercice25
#Ecrire un programme permettent de transposer une matrice carré
matrice=[
    [12, 4, 6],
    [3, 8, 74],
    [36, 13,41]
    ]
transposée=[[matrice[j][i] for j in range(len(matrice))] for i in range (len(matrice))]
print("la matrice transposée est :")
for ligne in transposée :
    print(ligne)
