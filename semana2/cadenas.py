s = "hola mundo"

for letra in s:
    print(letra, end="-")

for indice in range(len(s)):
    print(s[indice], end="-")

print()
print(s[0], type(s[0]))
print("Tamaño:", len(s))
'''
s[0] = "x"  # TypeError ya que el str es inmutable
'''

print("hola" + "mundo")
print("hola" "mundo")
print("-" * 4)
count_h = "Hola como estan usted hoy".lower().count("h")
print("Apariciones:", count_h)

print("Minusculas:", s.lower())
print("Mayusculas:", s.upper())
print("Capitalizado:", s.capitalize())
print("Reemplazar:", s.replace("hola", "adios"))
print("Reemplazar o por x:", s.replace("o", "x", 1).replace(" ", "-"))

