from django.urls import path, include
from .views import InscripcionView

app_name = 'inscripcion'
urlpatterns = [

    path('formulario', InscripcionView.as_view(), name='formulario'),

]
