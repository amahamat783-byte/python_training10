#Exercice 3:
#Ecrire un programme qui convertit un nombre entiers en secondes fourni au depart en un nombre d'années , mois , jours,  des minutes et des secondes (utilisé l'oeprateur %)
S=int(input('Entrez la valeur du seconde:'))
année=S//(365*24*3600)
S=S%(365*24*3600)
mois=S//(720*3600)
S=S%(720*3600)
jour=S//(24*3600)
S=S%(24*3600)
minute=S//60
seconde=S%60
print('année:',année,'mois:',mois,'jour:',jour,'minute:',minute,'seconde:',seconde)

