Dizionario = {1:"red", 2:"blue", 3:"green"}

while True:
    flag = input("inserire valore da 1 a 3: ")
    if flag == "fine":
        break
    
    print(Dizionario.get(int(flag), "errore"))
