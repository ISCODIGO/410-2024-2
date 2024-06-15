"""
1. pedir 3 parciales
2. obtener el promedio
3. regla:
    APR: prom >= 65
    RPB: 0 < prom < 65
        ABD: solo tiene un parcial
    NSP: prom == 0
"""
parcial1 = int(input("Parcial 1:"))
parcial2 = int(input("Parcial 2:"))
parcial3 = int(input("Parcial 3:"))

promedio = round((parcial1 + parcial2 + parcial3) / 3, 0)

if promedio >= 65:
    print("APR")
elif promedio > 0:
    # abandono -> dos parciales en cero
    abandonos = 0
    if parcial1 == 0:
        abandonos += 1
    if parcial2 == 0:
        abandonos += 1
    if parcial3 == 0:
        abandonos += 1

    if abandonos == 2:
        print("ABD")
    else:
        print("RPB")
else:
    print("NSP")

