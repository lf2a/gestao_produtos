from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Produto
from .form import ProdutoForm

def home(request):
    return render(request, 'home.html')

def deslogar(request):
    logout(request)
    return redirect('home')

@login_required
def produto_lista(request):
    produtos = Produto.objects.all()
    return render(request, 'lista.html', {'produtos': produtos})


@login_required
def produto_novo(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('produto_lista')

    return render(request, 'novo.html', {'form': form})


@login_required
def produto_altera(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('produto_lista')

    return render(request, 'novo.html', {'form': form})


@login_required
def produto_exclui(request, id):
    produto = get_object_or_404(Produto, pk=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('produto_lista')

    return render(request, 'exclui.html', {'produto': produto})