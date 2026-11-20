from django.db import models


class RegistroMetrica(models.Model):
    cpu = models.FloatField()
    ram = models.FloatField()
    temperatura = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Registro {self.id} - {self.fecha}"

