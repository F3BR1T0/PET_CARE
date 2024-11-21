from django.shortcuts import render
from django.views import View

class InicioView(View):
    def get(self, request):
        # Lógica para processar a requisição GET (por exemplo, renderizar um template)
        return render(request, 'pages/inicio.html')
