from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404 
from django.template import loader
from .models import Produto

# Create your views here.

def index(request):
    return HttpResponse("Blog index")
   
def detail(request, produto_id):
    return HttpResponse("Produto: %s." % produto_id)

def detail(request, produto_id):
    try:
        produto = Produto.objects.get(pk=produto_id)
    except Produto.DoesNotExist:
        raise Http404("Produto nao existe")
    return render(request, 'blog/detail.html', {'Produto': produto})

def content(request, produto_id):
    response = "Resultados da consulta %s."
    return HttpResponse(response % produto_id)

from .models import Produto

def index(request):
    produtosRecentes = Produto.objects.order_by('-data_cadastro')[:5]
    context = {'produtosRecentes': produtosRecentes}
    return render(request, 'blog/index.html', context)