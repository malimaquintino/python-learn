x = 0
while x < 10:
    if x == 3:
        x += 1
        continue

    if x == 8:
        break

    print(x)
    x += 1

y = 1
while y <= 10:
    print(y)
    y += 1
else: #se tiver um break não executa o else
    print('while else...')

print('program exit...')