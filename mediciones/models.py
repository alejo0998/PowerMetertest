import datetime
from django.db import models
from django.db.models import PROTECT


class Medidor(models.Model):
    llave_identificadora = models.CharField(max_length=100, null=False, unique=True)
    nombre = models.CharField(max_length=100, null=False)


class Medicion(models.Model):
    medidor = models.ForeignKey(
        Medidor, null=False, on_delete=PROTECT, related_name="medidor"
    )
    consumo_registrado = models.PositiveIntegerField(null=False)
    fecha_hora = models.DateTimeField(null=False, default=datetime.datetime.today)
