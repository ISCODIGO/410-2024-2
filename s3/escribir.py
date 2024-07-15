file_write = open("prueba1.txt", mode="w")
file_write.write("Programacion Orientada a Objetos\n")
file_write.write("22/06/2024\n")
file_write.writelines(
    [
        "Primer linea\n",
        "segunda linea\n",
        "Tercer linea\n"
    ]
)
file_write.close()
