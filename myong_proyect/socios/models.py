import uuid
from django.db import models

# Modelo para registrar socios de la ONG
class Socio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dni = models.CharField(max_length=15, unique=True, help_text="DNI o NIE del socio")
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    telefono = models.DecimalField(max_digits=9, decimal_places=0)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateField(auto_now_add=True)
    menor_edad = models.BooleanField()
    IBAN = models.CharField(max_length=34, blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"