from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Mapeia a URL raiz para a view de índice
    path('cadastro/', views.cadastro_paciente, name='cadastro_paciente'),
    path('listagem/', views.listagem_pacientes, name='listagem_pacientes'),
]
