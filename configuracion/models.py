from django.db import models


class Evento(models.Model):
    nombre = models.CharField(u"Nombre", max_length=50)
    cuenta = models.CharField(u"Cuenta", max_length=50)
    descripcion = models.TextField(u"Descripción")
    estado = models.BooleanField()

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.nombre


class Acceso(models.Model):
    token = models.TextField(u"Token")
    dominio = models.URLField(max_length=150)
    servicio = models.CharField(u"Servicio", max_length=50)
    estado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Acceso"
        verbose_name_plural = "Accesos"

    def __str__(self):
        return self.token
