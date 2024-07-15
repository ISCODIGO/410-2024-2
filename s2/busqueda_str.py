cadena = """El nombre de la función es type. La expresión entre paréntesis recibe el nombre de argumento de la función. El argumento es un valor o variable que se pasa a la función como parámetro de entrada. El resultado de la función type es el tipo del argumento.

Es habitual decir que una función “toma” (o recibe) un argumento y “retorna” (o devuelve) un resultado. El resultado se llama valor de retorno."""

print(cadena[0])
print(cadena[-1])
palabra = input("Palabra a buscar:")
encontrar1 = cadena.find(palabra)
print("Hallado:", encontrar1)
if encontrar1 >= 0:
    print("Segunda aparicion:", cadena.find(palabra, encontrar1 + 1))

print("Buscar inicio:", cadena.startswith("El"))
print("Buscar al final:", cadena.endswith("."))

t = "hola mundo"
# h | o | l | a |   | m | u | n | d | o
# 0   1   2   3   4   5   6   7   8   9
print(t[1:])

