from django.shortcuts import render
from django.views import View

class CadastrarInfo(View):
    def get(self, request):
        return render(request, 'pages/cadastrar_info.html')
