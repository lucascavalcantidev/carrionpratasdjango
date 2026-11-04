from django.shortcuts import render, get_object_or_404
from .models import Produto  
def index(request):
    """
   
    produtos = Produto.objects.all()
    
    contexto = {
        'produtos': produtos
    }
    return render(request, 'loja/joalheria.html', contexto)


def detalhe_produto(request, produto_id):
    """
    """
    produto = get_object_or_404(Produto, id=produto_id)
    
    contexto = {
        'produto': produto
    }
    return render(request, 'loja/detalhe.html', contexto)