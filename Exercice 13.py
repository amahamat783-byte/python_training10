#Exercice 13:
#Ecrire un programme (script) qui determine le nombre en occurence  de <<e>> dans une chaine.
chaine=input("sasir votre mot: ")
for caractere in chaine:
    if caractere=='e' or caractere=='é' or caractere=='è':
        nombres=chaine.count('e' )
        print("votre mot contient",nombres,"'e'")
        break
for caractere in chaine:
    if caractere=='é':
        nombres=chaine.count('é' )
        break
    print("votre mot contient",nombres,"'é'")
for caractere in chaine:
    if caractere=='è':
        nombres=chaine.count('è' )
        print("votre mot contient",nombres,"'è'")
