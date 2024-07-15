def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b;



f = sumar
print(f(1, 2))


def duplicar(funcion, a, b):
    return 2 * funcion(a, b)


print(duplicar(sumar, 2, 2))
print(duplicar(restar, 3, 5))
