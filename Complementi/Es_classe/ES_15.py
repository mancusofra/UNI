numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrare i numeri pari
numeri_pari = list(filter(lambda x: x % 2 == 0, numeri))
print(numeri_pari)  # Uscita: [2, 4, 6, 8, 10]

def f(i):
    return i**2

#Programma principale
print(list(map(f,numeri_pari)))