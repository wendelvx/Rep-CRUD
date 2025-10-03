from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

# Create your views here.

def lista_produtos(request):
    produtos=Produto.objects.all()
    return render(request, 'produto/lista.html', {'produtos':produtos})

def adicionar_produto(request):
    if request.method=='POST':
        form=ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form=ProdutoForm()
    return render(request, 'produto/adicionar.html', {'form':form})    