from cuid import cuid
from django.db import models

from processos.models import Processo


class Movimentacao(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=cuid)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE, related_name='movimentacoes')
    data_movimentacao = models.DateTimeField()
    descricao = models.TextField()
    tipo_movimentacao = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)