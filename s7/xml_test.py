import xml.etree.ElementTree as ET

archivo = open("persona.xml", "r")
datos = archivo.read()

arbol = ET.fromstring(datos)
print("Texto (email):", arbol.find("email").text)
print("Atributo (email):", arbol.find("email").get("oculto"))
