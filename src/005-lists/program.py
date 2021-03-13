list1 = [1, 2, 3, 4, 'abc', True]
print(list1)
print(list1[4])
print(list1[0:3])
print(list1[2:6])
print(list1[:4])  # do inicio até o 4
print(list1[2:])  # do 2 ao fim
print(list1[::2]) # exibe de 2 em 2

print('##########+###########')
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l3)

print('##########extend###########')
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
l1.extend('a')
print(l1)

print('##########apend###########')
l1 = [1, 2, 3]
l1.append('a') # add no final
print(l1)

print('##########insert###########')
l1 = [1, 2, 3]
l1.insert(2, 'a') # add no indice informado
print(l1)


print('##########pop###########')
l1 = [1, 2, 3]
l1.pop() # remove do final
print(l1)

print('##########del###########')
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del(l1[2])
print(l1)
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del(l1[3:5])
print(l1)

print('##########max and min value###########')
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(l1))
print(min(l1))

print('##########range###########')
l1 = list(range(0, 100, 5)) # de 0 a 100 multiplos de 5
print(l1)
l1 = list(range(10))
print(l1)

