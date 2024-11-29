from cuid import cuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UsuarioManager(BaseUserManager):
    def create_user(self, email, cpf, nome, senha=None, **extra_fields):
        if not email:
            raise ValueError('O campo Email é obrigatório')
        if not cpf:
            raise ValueError('O campo CPF é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, cpf=cpf, nome=nome, **extra_fields)
        user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, cpf, nome, senha=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, cpf, nome, senha, **extra_fields)

class Usuario(AbstractBaseUser):
    id = models.CharField(primary_key=True, max_length=36, default=cuid, editable=False)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=255)
    password = models.CharField(max_length=255, default='qwertyuiop')  # Defina um valor padrão
    role = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    foto = models.CharField(max_length=255, blank=True, default='assets/images/avatar.webp')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cpf', 'nome']

    def __str__(self):
        return self.nome