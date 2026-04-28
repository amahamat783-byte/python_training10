#Exercice 20
#Parité des elements d'un tableau
Tab=[]
n=int(input("veuillez saisir les nombres de cases: "))
paire=[]
impaire=[]
for i in range (n):
    element=int(input("veuillez saisir la valeur des elements: "))
    Tab.append(element)
print(Tab)
for i in range  (n):
    if  Tab[i]%2==0:
        paire.append(Tab[i])
    else:
     impaire.append(Tab[i])
print("les éléments pairs du tableau sont:",paire)
print("et les éléments imppairs sont:", impaire)
