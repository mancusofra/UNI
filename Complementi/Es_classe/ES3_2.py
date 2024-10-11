flag = int(input("inserire valore da 1 a 3: "))
Dizionario = {1:"red", 2:"blue", 3:"green"}

if flag in Dizionario:
    print(Dizionario[flag])

else:
    print("errore")
