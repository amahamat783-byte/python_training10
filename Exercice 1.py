import math
print("entrer la valeur de a")
a=float(input())
print("entrer la valeurn de b")
b=float(input())
print("entrer la valeur de c")
c=float(input())

if a==0 :
    print("c'est une équation du premier degré")
    if b==0:
        if c==0:
          print("mais Comme les valeurs que vous aviez attribué à b et à c sont nulles alors L'équation  admet une infinité de solutions ")
        else:
          print("mais Etant donné la valeur de b que vous avez saisi est nulle alors L'équation  n'admet pas de solutuions ")
    else:
      print(" qui a pour solution: X =",-c/b)
elif ((a!=0) and (b==0) and (c!=0)):
    print("c'est une équation de second dégré sans second membre")
    if (c<0):
        print(" qui admet deux solution x=",-c/math.sqrt(a), "ou x=",c/math.sqrt(a))
    else:
        print("et comme le carrée d'un nombre n'est jamais négatif alors elle n'admet pas de solution dans R")
else:
    D=b**2-4*a*c
    if D<0:
      print(" la valeur de delta est strictement inferieur à 0 alors y'a pas de solution dans R")
    elif D>0:
        print("L'equation admet deux solutions distinctes qui sont: X1=",-b-(math.sqrt(D))/2*a, "et X2=", (-b+(math.sqrt(D))/2*a))
    else:
        print("L'equation admet une solution double x:X0=", -b/2*a)
