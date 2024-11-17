from django.urls import path
from .pages import BemVindoView

urlpatterns = [
    path('', BemVindoView.as_view(), name='bem_vindo'),  # Página inicial
]
