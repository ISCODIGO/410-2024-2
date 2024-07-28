# Para ejecutar este programa descarga BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# O descarga el archivo
# http://www.py4e.com/code3/bs4.zip
# y descomprimelo en el mismo directorio que este archivo

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl


def buscar_links(bsoup: BeautifulSoup):
    # Recuperar todas las etiquetas de anclaje
    etiquetas = bsoup("a")
    for etiqueta in etiquetas:
        print(etiqueta.get("href", None))


def buscar_imagenes(bsoup: BeautifulSoup):
    imagenes = bsoup("img")
    for img in imagenes:
        print(img.get("src", None))


def buscar_banner(bsoup: BeautifulSoup):
    div = bsoup.find("div", {"class": "sb-msg"})
    h4 = div.find("h4")
    p = div.find("p")
    print(h4)
    print("-" * 10)
    print(p)


# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Introduzca URL: ")
html = urllib.request.urlopen(url, context=ctx).read()


sopa = BeautifulSoup(html, "html.parser")
buscar_banner(sopa)
