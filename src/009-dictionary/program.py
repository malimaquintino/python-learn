import copy

dictionary = {'key1': 'value1', 'key2': 'value2'}
dictionary['key3'] = 'value3'
print(dictionary)
print(dictionary['key1'])

d1 = dict(key1='val1', key2='val2')
print(d1)

d2 = {
    'str': 'string as key',
    12345: 'int as key',
    (1, 2, 3): 'tuple as key'
}
print(d2)
print(d2[(1, 2, 3)])

# check key in dictionary
print(d2.get('no_key'))
# d2['no_key'] key not exist return error
if d2.get('no_key') is None:
    print('create key')

if 'no_key' not in d2:
    print('create key')

# check value in dictionary
print('int as key' in d2.values())
print(len(d2))

print()
print('loop keys')
for k in d2:
    print(k)

print()
print('loop values')
for v in d2.values():
    print(v)

print()
print('loop key value')
for i in d2.items():
    print(i)
    print(i[0], ' => ', i[1])

print()
print('loop key value 2')
for k, v in d2.items():
    print(k, '=>', v)

print()
print('sub dictionary')
d3 = {
    'person1': {
        'name': 'Anna',
        'lastname': 'Mag'
    },
    'person2': {
        'name': 'Lois',
        'lastname': 'Clarck'
    },
}
for pk, pv in d3.items():
    print(pk)
    for vk, vv in pv.items():
        print(f'\t{vk} => {vv}')

print()
print('assignment the dictionary they point to same object ')
d4 = {1:'a', 2:'b', 3:'c'}
d5 = d4
d5[1] = 'abc'
print(d4)
print(d5)

print()
print('use deepcopy to have identical dictionary ')
d5 = copy.deepcopy(d4)
d5[1] = 'xpt'
print(d4)
print(d5)

