def f():
    def g():
        print('help')
    return g
res = f()
print(res)