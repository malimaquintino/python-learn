# func anonima
multiply = lambda a, b: a * b
print(multiply(2, 2))

my_list = [
    ['p1', 10],
    ['p2', 8],
    ['p3', 13],
    ['p4', 5],
]

print(my_list)


def key_to_order(item):
    return item[1]

#sort altera o array
my_list.sort(key=key_to_order)
print(my_list)

my_list.sort(key=key_to_order, reverse=True)
print(my_list)

my_list.sort(key=lambda item: item[1])
print(my_list)

#sorted não altera o array
print(sorted(my_list))
print(sorted(my_list, key=lambda i: i[1]))
print(sorted(my_list, key=lambda i: i[1], reverse=True))