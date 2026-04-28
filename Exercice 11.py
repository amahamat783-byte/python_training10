#Exercice11
#Histoire du jeu d'echec et la recompence du vieux avec du riz
n=64
grains=1
for i in range(1, n+1) :
    print(f"cases : {i}")
    print(f"graines : {grains}")
    print(f"graines notaion scientifiques : {grains :.2e}")
    grains=grains*2
