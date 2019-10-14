from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    edad = models.IntegerField(default=0)
    estudios = models.CharField(max_length=200)
    

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField('fecha para la reserva')


class Reserva_Material(models.Model):
    reserva_id = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)


class Material(models.Model):
    producto = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=1000)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)


class Aula(models.Model):
    planta = models.CharField(max_length=50)
    mida = models.CharField(max_length=50)
    disponibilidad = models.CharField(max_length=100)
