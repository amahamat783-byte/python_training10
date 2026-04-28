#Exercice4
#Un algorithme qui affiche les 20 premiers termes de la table de multiplication par 7, en signalant au passage(à l'aide d'une asterisque ) ceux qui sont multiples de 3.
Tab=[20]
print("Parmi les", 20," prémiers termes multplier par  7, tous ceux dans l'asterisque sont  les multiples de 3 ")
for i in range(1, 21):
    i=i*7
    if i%3==0:
        print(f"{i}*")
    else:
        print(i)
