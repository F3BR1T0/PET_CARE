from django.shortcuts import render
from django.views import View

class CadastrarConta(View):
    def get(self, request):
        return render(request, 'pages/cadastrar_conta.html')
