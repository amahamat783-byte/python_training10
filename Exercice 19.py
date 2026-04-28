#Exercice 19:
#le maximun des elements d'un tableau
Tab=[]
n=int(input("veuillez saisir les nombres de cases: "))
maxi=0
for i in range (n):
    element=int(input("veuillez saisir la valeur des elements: "))
    Tab.append(element)
print(Tab)
for i in range  (n):
    print(Tab[i])
for i in range  (n):
    if maxi<=Tab[i]:
        maxi=Tab[i]
print("le maximun est:", maxi)
