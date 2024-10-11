def inserisci_valori():
    valore = input("Inserisci un valore (oppure '#' per terminare): ")
    if valore == '#':
        return []
    else:
        return [valore] + int(inserisci_valori())

def f(i):
    return i**2

# Programma principale
l = inserisci_valori()


print(list(map(f,l)))