Testo = input("iniserire testo: ")
Diz = {}
for i in Testo:

    if i not in Diz:
        new = {i:0}
        Diz.update(new)
    
    Diz[i] += 1

print(sorted(Diz))

'''Testo = input("iniserire testo: ")
Diz = {}
for i in range(len(Testo)):

    if Testo[i] not in Diz:
        new = {Testo[i]:0}
        Diz.update(new)
    
    Diz[Testo[i]] += 1

print(Diz) '''