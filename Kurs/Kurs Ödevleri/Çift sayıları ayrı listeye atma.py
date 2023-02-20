liste = [i for i in range(1,101) if i % 2 == 0]
print(liste)

# ya da

liste = list(range(1,101))
liste1 = []
for i in liste:
    if(i % 2 == 0):
        liste1.append(i)
print(liste1)
