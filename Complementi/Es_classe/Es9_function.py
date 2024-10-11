lista = [[1,2,3], [4,5,6]]

def Appiatire(lis, stringa=''):
    if len(lis) == 0:
        return stringa
    
    flag = lis[0]
    print(*flag)
    #stringa = stringa + str(*flag)
    Appiatire(lis[-(len(lis)-1):], stringa)


print(Appiatire(lista))