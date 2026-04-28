#Exercice21
#Ecrire un programme qui permet d'analyser un par un tous les éléments présent d'une liste des mots et les séparer en deux selon la longeur des mots 
mot=['Jean','Maximilien','Brigitte','Sonia','Jean-Pierre','Sandra']
moins_de_6=[ nom for nom in mot if len(nom)<6]
plus_ou_egal_6=[ nom for nom in mot if len(nom)>=6]
print("les mot a moins de 6 caractèes sont :", moins_de_6)
print("les mot avec 6 caractèes ou plus sont :",plus_ou_egal_6 )
