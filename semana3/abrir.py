# crear el manejar de fichero (file handler)
file = open("mbox.txt")


# linea = 0
# for texto in file:
#     print(f"Linea: {linea}", texto)
#     linea += 1


# lectura = file.read(255)
# print("Ha leido algo???", lectura)

# print("----- Segunda lectura -----")

# lectura = file.read(255)
# print("Ha leido algo???", lectura)

lineas = file.readline()
print(len(lineas))

file.close()
