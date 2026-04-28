Tab=[]
for i in range (n):
    element=n-j
    j=j-1
    Tab.append(element)
print(Tab)
j=1
for i in range  (n):
    Tab[i]=i*2
    Tab[0]=Tab[0]+1
    print(Tab[i])
for i in range  (n):
    som=som+Tab[i]
print("lasomme est",som)
"""
print("le maximun est:", maxi)
mini=Tab[i]
for i in range  (n):
    if mini>Tab[i]:
        mini=Tab[i]
print("le minimun est:", mini)
"""
