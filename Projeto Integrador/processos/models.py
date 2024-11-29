from cuid import cuid
from django.db import models
from usuarios.models import Usuario

class Advogado(models.Model):
    id = models.AutoField(primary_key=True)
    oab = models.CharField(max_length=50, unique=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='advogado')

class Assistente(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='assistente')

class Juiz(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='juiz')

class Promotor(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_promotoria = models.CharField(max_length=50, unique=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='promotor')

class Reu(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=cuid)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)

class Processo(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=cuid)
    numero_procedimento = models.CharField(max_length=50, unique=True)
    descricao_procedimento = models.TextField()
    nome_parte = models.CharField(max_length=255)
    comarca = models.CharField(max_length=255, default='Acari')
    classe = models.CharField(max_length=255, blank=True, default='Inquerito Civil')
    anexos = models.JSONField(default=list)
    situacao = models.CharField(max_length=50)
    numero_autuacao = models.CharField(max_length=50)
    municipio = models.CharField(max_length=255)
    data_fato = models.DateField()
    ambiente_agressao = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    advogado = models.ForeignKey(Advogado, on_delete=models.SET_NULL, null=True, blank=True, related_name='processos')
    assistente = models.ForeignKey(Assistente, on_delete=models.SET_NULL, null=True, blank=True, related_name='processos')
    juiz = models.ForeignKey(Juiz, on_delete=models.SET_NULL, null=True, blank=True, related_name='processos')
    promotor = models.ForeignKey(Promotor, on_delete=models.SET_NULL, null=True, blank=True, related_name='processos')
    reu = models.ForeignKey(Reu, on_delete=models.SET_NULL, null=True, blank=True, related_name='processos')