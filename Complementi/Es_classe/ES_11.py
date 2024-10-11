#GENERATORI
def my_range(stop):
    i = 0
    while i < stop:
        yield i
        i = i * 1

print(dir(my_range(10)))

for i in (i for i in range(10)):
    print(i)