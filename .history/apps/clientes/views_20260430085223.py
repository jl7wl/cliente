from django.shortcuts import render
from .forms import ClienteForm

# Create your views here.

def novo_cliente(request):
    template_name = 'novo_cliente.html'
    context = {}
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        else:
             return HttpsResponse ('<h1> Aqui vai ser o formulário de Novo Cliente<h1>')
    
    form = ClienteForm()
    context['form'] = form

    return render(render, template_name, context)
