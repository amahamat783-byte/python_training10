#Exercice26
#Ecrire un programme qui permet de faire la multiplication de deux matrices
A=[
    [8, 2],
    [14, 10]
    ]
B=[
    [5, 3],
    [9, 1]
    ]
L, C= len(A) , len(B[0])
p=[[0]* C for _ in range(L)]
for i in range (L) :
    for j in range (C) :
        for k in range (len(B)) :
            p[i][j]+=A[i][k]*B[k][j]
print("le produit des matrices :")
for ligne in p :
    print(ligne)
    
