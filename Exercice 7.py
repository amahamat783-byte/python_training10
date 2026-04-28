#Exercice7
#Ecrire un programme de convertir un angle donné en degrés , minutes et sécondes en radians
import math
d= int(input("entrer les degres : "))
m= int(input("entrer les minutes : "))
s=int(input("entrer les secondes : "))
AD=d+(m/60)+(s/3600)
rad=(AD*math.pi)/180
print("l'angle en radians est : ", rad)
