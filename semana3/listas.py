lista = []
lista = list()
lista = [1, 2, 3, 4, 5, "Hola", True, [1, 2, 3]]

print(lista[0])  # 1
print(lista[7])  # [1, 2, 3]
print(lista[7][2])  # 3

print("Recorrido por for...")
for elemento in lista:
    print(elemento)

print("cuantos elementos hay en la lista?", len(lista))

lista2 = ["hola", "adios", "objetos", "programacion"]
entrada = input("Buscar elemento:")
if entrada in lista2:
    print("Palabra encontrada:", entrada)
else:
    print("Palabra no se encontro")
