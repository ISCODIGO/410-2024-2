import xml.etree.ElementTree as ET

archivo = open("persona.xml", "r")
datos = archivo.read()

arbol = ET.fromstring(datos)
print("Nombre:", arbol.find("nombre").text)
print("Atributo:", arbol.find("email").get("oculto"))
