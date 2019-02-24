from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .models import Acceso
from .forms import AccesoModelForm


class AccesoListView(ListView):
    model = Acceso
    template_name = "configuracion/acceso/list.html"


class AccesoCreateView(CreateView):
    model = Acceso
    template_name = "configuracion/acceso/form.html"
    form_class = AccesoModelForm
    success_url = reverse_lazy("configuracion:acceso_listar")


class AccesoUpdateView(UpdateView):
    model = AccesoModelForm
    template_name = "configuracion/acceso/form.html"
    form_class = AccesoModelForm
    success_url = reverse_lazy("configuracion:acceso_listar")
