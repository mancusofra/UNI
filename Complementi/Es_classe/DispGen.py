def Generatore_disp(Num):
    for i in range(Num):
        if(i%2):
            yield i

#È un iggetto non esegue la funzione che gli passi automaticamente
lista = (i for i in range(10) if (i%2)!=0)
print(list(lista))