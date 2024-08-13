from django.db import models

# Create your models here.
class Cliente(models.Model):
    identidad = models.CharField("Cédula", max_length=15)
    primer_nombre = models.CharField("Primer nombre", max_length=30)
    primer_apellido = models.CharField("Primer apellido", max_length=30)
    direccion = models.TextField("Dirección")
    telefono = models.CharField("Telefono", max_length=20)
    email = models.EmailField("Email")

    class Meta:
        db_name