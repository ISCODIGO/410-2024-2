from urllib.request import urlopen

recurso = urlopen('http://data.pr4e.org/romeo.txt')
for linea in recurso:
    print(linea.decode().strip())


imagen = urlopen("http://data.pr4e.org/cover3.jpg")
archivo = open("archivo.jpg", "wb")
archivo.write(imagen.read())
