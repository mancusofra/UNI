x = 0 

def f(x):
    if x>0:
        print(x)
    else:
        raise Exception

try:
    f(x)
    print('tutto ok')
except Exception as e:
    print(f'Exeption: {e}')

else:
    print('Else')

finally:
    print('finaly!!')