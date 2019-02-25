from django.urls import path, include

from inscripcion.views import EventoDetailView
from .views import EventoView

app_name = 'inscripcion'
urlpatterns = [

    path('eventos', EventoView.as_view(), name='eventos'),
    path('evento/<slug:pk>', EventoDetailView.as_view(), name='formulario'),
]
