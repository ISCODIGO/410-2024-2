# while
x = 10
while x > 0:
    x -= 1
    if x % 2 == 0:
        continue
    print(x)

print('Impresion de y')
y = 3
bandera = True
while bandera:
    if y == 0:
        bandera = False
    print(y)
    y -= 1
