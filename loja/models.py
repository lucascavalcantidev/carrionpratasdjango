from django.db import models

from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.URLField(blank=True, null=True)  # Suporta links de imagens diretos

    def __str__(self):
        return self.nome
