from django.shortcuts import render
from django.views.generic import TemplateView
import requests


class IdexTemplateView(TemplateView):
    template_name = 'inscripcion/index.html'


class InscripcionView(TemplateView):
    template_name = "inscripcion/view.html"

    def get_context_data(self, **kwargs):
        context = super(InscripcionView, self).get_context_data(**kwargs)
        r = requests.get("http://localhost:9000/payment/112/222/", headers={
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgyNTA0MTg3LCJqdGkiOiIwZGQ1MDczN2Q2ZmU0ZmM0OTdiMmZhYTkyNGIwN2EzMSIsInVzZXJfaWQiOjF9.W3v1NQp2ctBr9SVXlWI6QdyFiMbqD9AFfl_nSNYzEts'})
        print(r.json())
        return context
