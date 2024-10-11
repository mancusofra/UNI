def f(arg1,arg2=0): #in python rendiamo un argomnto opzionale se li passiamo un valore di default
    print(f'arg1: {arg1}, arg2: {arg2}')
    #Possimao fargli ritornare dei return multipli
    return True, False, 'uccidetemi'

'''    
res=f('ciao', 3)
print(res)

res=f('ciao2')
print(res)
'''

#l'asterisco permette di srotolare gli elementi di una lista 
# --> possiamo passare come parametri gli elementi di una lista
l1 = ['pippo', 2]
print(*l1)
f(*l1)

#Stessa cosa anche per i dizzionari in cui posso anche associare la keyword dei dizionari 
#al nome del parametro
d1 = {'arg2':'pluto', 'arg1':42}
f(**d1)
