#Exercice23
#Ecrire un programme qui permet de faire la somme des éléments d'une matrice
matrice=[
    [2,4,6],
    [14,10,3]
    ]
somme=sum(sum(ligne) for ligne in matrice )
print("la somme des éléments est :", somme)
