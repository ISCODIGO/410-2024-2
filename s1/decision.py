try:
    x = int(input("Escriba un numero:"))
except ValueError:
    print("No es un numero valido")
else:
    if x % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
print("Fin del programa")
