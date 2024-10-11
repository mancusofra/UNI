Rubrica = {}
while True:
    flag = int(input("1-inserisci \n2-cancella \n3-stampa\n >>"))
    if flag == 1:
        Nome = input("inserire nome >> ")
        Numero = input("inserire numero >> ")
        New = {Nome:Numero}
        Rubrica.update(New)
    if flag == 2:
        Nome = input("inserire nome da eliminare >> ")
        Rubrica.pop(Nome)
    elif flag == 3:
        print(Rubrica)

    