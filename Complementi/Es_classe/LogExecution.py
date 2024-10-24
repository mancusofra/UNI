import datetime

def mio_decoratore(func):
    def funzione_interna(*args, **kwargs):
        data_ora_corrente = datetime.datetime.now()
        with open("/home/francesco/UNI/Complementi/Es_classe/FileLog/Execution_log.txt", "a+") as file:
            file.write(f"Esecuzione svolta: {data_ora_corrente}.\n")

        print("Scrittura completata.")
        return func(*args, **kwargs)
    return funzione_interna

@mio_decoratore
def somma(*valori:int):
    return sum(valori)

Numeri = [1,2,3]
print(somma(*Numeri))
