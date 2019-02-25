from django.contrib import admin

from .models import Evento, Acceso


@admin.register(Acceso)
class AccesoAdmin(admin.ModelAdmin):
    pass


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cuenta", "estado")
