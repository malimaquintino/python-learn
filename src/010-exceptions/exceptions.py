try:
    b={}
    print(b['ioioio'])
    print(a)
except NameError as e:
    print('erro:', e)
except Exception as e:
    print('erro:', e)
else:
    print('it runs if try no get errors')
finally:
    print('it always run')

print('keep it..')