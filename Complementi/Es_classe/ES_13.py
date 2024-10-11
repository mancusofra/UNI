def d_f(f):
    def function(*args, **kwargs):
        return f(*args, **kwargs)
    return function

@d_f    
def pippo(x, y, z):
    print(x)
    print(y)
    print(z)
d_f
pippo(x=1,y=2,z=3)