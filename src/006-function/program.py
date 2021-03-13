def myFunction(msg, loop=10):
    i = 0
    while i < loop:
        print(msg)
        i += 1


def returnFunction(value1, value2):
    return value1 + value2

def fArgs(*args):
    print(args)

def fArgs2(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['name'], kwargs['lastName'])
    print(kwargs.get('name'), kwargs.get('age')) # utilizar get


myFunction('test1')
print()
myFunction('test2', 5)
print()
myFunction(loop=8, msg='hi')
print()
print(returnFunction(1, 2))
print()
fArgs(1, 3, 'abnm', '200')
print()
fArgs2(1, 2, 3, 4, name='Joseph', lastName='Smith')
