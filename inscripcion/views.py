from django.shortcuts import render
from django.views.generic import TemplateView
import requests

from configuracion.models import Acceso, Evento
from configuracion.views import AccesoUpdateView


class IdexTemplateView(TemplateView):
    template_name = 'inscripcion/index.html'


class InscripcionView(TemplateView):
    template_name = "inscripcion/view.html"

    def get_context_data(self, **kwargs):
        context = super(InscripcionView, self).get_context_data(**kwargs)
        dni = self.request.GET.get("dni")
        evento_id = self.request.GET.get("evento")

        evento = Evento.objects.get(id=evento_id)

        acceso = Acceso.objects.filter(estado=True)[0]
        url = acceso.dominio + acceso.servicio + "/" + dni + "/" + evento.cueenta + "/"
        r = requests.get(url, headers={
            'Authorization': "%s %s" % ("Bearer", acceso.token)})
        print(r.json())
        return context
