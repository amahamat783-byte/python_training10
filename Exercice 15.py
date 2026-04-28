#Exercice15
#Un algorithme qui affiche recopie l'inverse une chaine
Tab=[]
chaine=input("saisir votre mot")
for i in chaine:
    c_inverse=chaine[::-1]
print(f"{c_inverse}")
