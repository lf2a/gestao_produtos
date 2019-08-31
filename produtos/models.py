from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField()
    vencimento = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.nome
