'''
def concatenate_strings(*stringhe:str, Separator:str='-'):
    flag=stringhe[0]
    for arg in stringhe[1:]:
        flag+=Separator + arg
    return flag

print(concatenate_strings("dio", Separator=" super "))
'''

from functools import reduce

# Definiamo una funzione che somma due numeri
def concatenate_strings(a, b, Separator="-"):
    return a + Separator + b

# Lista di numeri
parole = ["ciao", "ciaooo"]

# Riduciamo la lista usando la funzione somma
risultato = reduce(concatenate_strings, parole)

print(risultato)  # Output: 15
