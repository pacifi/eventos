from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
import requests

from configuracion.models import Acceso, Evento
from configuracion.views import AccesoUpdateView


class IdexTemplateView(TemplateView):
    template_name = 'inscripcion/index.html'


class EventoView(TemplateView):
    template_name = "inscripcion/view.html"

    def get_context_data(self, **kwargs):
        context = super(EventoView, self).get_context_data(**kwargs)
        # dni = self.request.GET.get("dni")
        # evento_id = self.request.GET.get("evento")
        #
        # evento = Evento.objects.get(id=evento_id)
        #
        # acceso = Acceso.objects.filter(estado=True)[0]
        # url = acceso.dominio + acceso.servicio + "/" + dni + "/" + evento.cueenta + "/"
        # r = requests.get(url, headers={
        #     'Authorization': "%s %s" % ("Bearer", acceso.token)})
        # print(r.json())
        context['eventos'] = Evento.objects.filter(estado=True)

        return context


class EventoDetailView(DetailView):
    model = Evento
    template_name = "inscripcion/detail.html"

    def get_context_data(self, **kwargs):
        context = super(EventoDetailView, self).get_context_data(**kwargs)
        documento = self.request.GET.get("documento")
        if documento:
            print(self.get_object())
            acceso = Acceso.objects.filter(estado=True)[0]
            url = acceso.dominio + acceso.servicio + "/" + documento + "/" + self.get_object().cuenta + "/"
            r = requests.get(url, headers={
                'Authorization': "%s %s" % ("Bearer", acceso.token)})
            print(r)
            print(r.json())
            context['pago'] = r.json()
        return context
