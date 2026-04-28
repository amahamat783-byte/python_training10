#Exercice12
#Ecrire un programme (script) qui determine si une chaine contient un <<e>> .
chaine=input("Veuillez saisir une chaine de caractères: ")
for caractere in chaine:  
    if caractere=='e':
        print("la chaine admet le caractère 'e'.")
        break
else:
    print("la chaine n'admet pas le caractère 'e'.")
 
    
    
