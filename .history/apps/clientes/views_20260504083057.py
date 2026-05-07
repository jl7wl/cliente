from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ClienteForm
from .models import Cliente
# Create your views here.

def novo_cliente(request):
    clientes = Cliente.objects.all()
    template_name = 'novo_cliente.html'
    context = {}
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('novo_cliente')
        else:
             return HttpsResponse ('<h1> Aqui vai ser o formulário de Novo Cliente<h1>')
    
    form = ClienteForm()
    context['form'] = form
    context['clientes'] = clientes
    return render(request, template_name, context)

def atualizar_cliente(request, id):
    try:
        cliente = 