from django.shortcuts import render
from .forms import ClienteForm

# Create your views here.

def novo_cliente(request):
    template_name = 'novo_cliente.html'
    if request.method == 'POST':
    return "<h1> Aqui vai ser o formulário de Novo Cliente"