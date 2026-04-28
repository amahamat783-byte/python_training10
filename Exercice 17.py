#Exercice 17:
t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t2=['janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Decembre']
t3=[]
for mois, jours in zip(t2,t1):
    t3.append(mois)
    t3.append( jours)
print("la troisieme liste est:",t3)
