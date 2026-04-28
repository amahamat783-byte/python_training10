#Exercice 9
# temperature
print("vous souhaitez convertir la temperature en degre celsius ou en degre fahrenheit?")
while True:
    choix=input()
    if choix=="C" or choix=="c" or choix=="F" or choix=="f":
        break
    print("S'il vous plait! saisissez C ou c pour le degre celsus. F ou f pour degre fahrenheit")
if choix=="C" or choix=="c":
    TF=int(input("Saisir la valeur de la temperature en degre fahrenheit: "))
    TC=(TF-32)*5/9
    print("la temperature de", TF,"en degre  celsus est:",TC)
elif choix=="F" or choix=="f":
    TC=int(input("Saisir la valeur de la temperature en degre celsius: "))
    TF=(TC*9/5)+32
    print("la temperature de", TC,"°","en degre fahrenheit est:",TF)
