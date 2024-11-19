from django.urls import path
from .pages import *

urlpatterns = [
    path('', BemVindoView.as_view(), name='bem_vindo'),  # Página inicial
    path('cadastrar/conta', CadastrarConta.as_view(), name="cadastrar_conta"),
    path('cadastrar/informacoes', CadastrarInfo.as_view(), name="cadastrar_info")
]
