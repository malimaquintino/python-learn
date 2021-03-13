text = 'python'
for word in text:
    print(word)
print()

for i, word in enumerate(text):
    print(i, word)
print()

for n in range(10):
    print(n)
print()

for n in range(10, 100, 5):
    print(n)
print()

for n in range(10, 0, -1):
    print(n)
print()

for n in range(10):
    if n == 3:
        continue

    if n == 7:
        break
    print(n)
print()