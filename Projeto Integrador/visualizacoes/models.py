from cuid import cuid
from django.db import models
from django.utils.timezone import now

from processos.models import Processo
from usuarios.models import Usuario


class Visualizacao(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=cuid)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE, related_name='visualizacoes')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='visualizacoes')
    data_visualizacao = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)