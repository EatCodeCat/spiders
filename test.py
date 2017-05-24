from collections import Iterable

def y():

    yield 1
    yield 2
    yield 'sd'
    return  'xxxxxxxxx'

if __name__ == '__main__':
    for i in y():
        print (i)

    print( isinstance(y(), Iterable))
    print(y())