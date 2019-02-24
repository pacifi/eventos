from django.urls import path, include
from .views import AccesoListView, AccesoCreateView, AccesoUpdateView

app_name = 'cofiguracion'
urlpatterns = [

    path('acceso/listar', AccesoListView.as_view(), name='acceso_listar'),
    path('acceso/crear', AccesoCreateView.as_view(), name='acceso_crear'),
    path('acceso/actualizar/<int:pk>', AccesoUpdateView.as_view(), name='acceso_actualizar'),

]
