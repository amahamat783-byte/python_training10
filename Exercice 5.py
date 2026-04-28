#Exercice5
#Un algorithme qui  fait les 50 multiples de 13 et n'affiche que les multiples de 7.
print("Jusqu'à combien fois souhaitez-vous multiplier l'entier 13? " )
N=int(input())
print("Parmi les", N," termes multplier par 13, les multiples de 7 sont: ")
for i in range(1, N+1):
    i=i*13
    if i%7==0:
         print(i)
