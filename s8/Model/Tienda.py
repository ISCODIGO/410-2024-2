#!/usr/bin/python
#-*- coding: utf-8 -*-

class Tienda:
    estatico = "hola"

    def __init__(self):
        self.direccion = None
        self.nombre = None
        self.telefonos = None
        self.Attribute1 = None

    def f1(self):
        self.xyz = 0


t = Tienda()
t.f1()
print(t.__dict__)
print(Tienda.__dict__)
