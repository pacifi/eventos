from django.db import models


class Evento(models.Model):
    nombre = models.CharField(u"Nombre", max_length=50)
    cueenta = models.CharField(u"Cuenta", max_length=50)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.nombre


class Acceso(models.Model):
    token = models.CharField(u"Token", max_length=50)
    dominio = models.URLField()
    servicio = models.CharField(u"Servicio", max_length=50)
    estado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Acceso"
        verbose_name_plural = "Accesos"

    def __str__(self):
        return self.token
