#Exercice22
#Ecrire un programme qui permet :
#saisir les élements d'un tableau à deux dimensions (matrice) de L lignes et C colones
#puis afficher les élements
L=int(input("entrer les nombres des lignes :"))
C=int(input("entrer les nombres des colones :"))
matrice=[]
for i in range(L) :
    ligne=[]
    for j in range(C) :
        val=int(input(f"entrer l'élement[{i}{j}] :"))
        ligne.append(val)
        matrice.append(ligne)
print("la matrice saisie est :")
for ligne in matrice :
    print(ligne)
