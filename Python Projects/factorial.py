from math import factorial


def f(n):

    f=1

    for i in range(n):
        f*=i+1
    
    return f

    print(f(0))

