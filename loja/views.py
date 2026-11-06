import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    contexto = {'produtos': produtos}
    return render(request, 'loja/joalheria.html', contexto)

def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    contexto = {'produto': produto}
    return render(request, 'loja/detalhe.html', contexto)

@csrf_exempt
def api_chat(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            opcao = str(dados.get('opcao', '')).strip()

            if opcao == '1':
                resposta = 'As nossas formas de pagamento incluem Pix, cartão de crédito e boleto.'
            elif opcao == '2':
                resposta = 'O nosso raio de entrega atende apenas a região de São Paulo Capital.'
            elif opcao == '3':
                resposta = 'O prazo médio de entrega é de 2 a 5 dias úteis para SP Capital.'
            elif opcao == '4':
                resposta = 'Você pode tirar dúvidas frequentes sobre garantia, trocas e cuidados com a prata diretamente com a gente!'
            elif opcao == '5':
                resposta = 'Atendimento encerrado com sucesso. Obrigado por visitar a Carrion Pratas! 👋'
            else:
                resposta = 'Olá! Sou a assistente virtual da joalheria Carrion Pratas. Como posso ajudar?'

            return JsonResponse({'resposta': resposta})
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)

    return JsonResponse({'erro': 'Método não permitido'}, status=405)