# sumar digitos
# in: 1234
# out: 10

valor = input("Escriba un numero:")
# suma = 0
# for x in valor:
#     suma += int(x)
# print("La suma de los digitos es:", suma)

# definir si un numero es primo
# primo es divisible por 1 y por si mismo

numero = int(valor)
es_primo = True
for d in range(2, numero):
    if numero % d == 0:
        es_primo = False
        break
if es_primo:
    print("Es primo")
else:
    print("No es primo")
