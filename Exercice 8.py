#Exercice8
#Ecrire un programme de convertir un angle donné radians en degrés , minutes et sécondes.
import math
rad=float(input("entrer l'angle en radians: "))
d=((rad*180)/math.pi)
m=(d-int(d))*60
s=(m-int(m))*60
print("le degre est:",int(d),",les minutes",int(m),"et sécondes",int(s))
