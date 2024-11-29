from django import forms
from django.contrib.auth import authenticate
from .models import Usuario

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='EMAIL',
        widget=forms.EmailInput(attrs={
            'class': 'entrada-input input-box', 
            'placeholder': 'Digite seu email',
            'required': True,
            'autocomplete': 'off',
            'value': ''# Adiciona o atributo autocomplete
        })
    )
    
    senha = forms.CharField(
        label='SENHA',
        widget=forms.PasswordInput(attrs={
            'class': 'entrada-input input-box', 
            'placeholder': 'Digite sua senha',
            'required': True,
            'autocomplete': 'off',
            'value': ''# Adiciona o atributo autocomplete
        })
    )

    def clean(self):
        email = self.cleaned_data.get('email')
        senha = self.cleaned_data.get('senha')
        
        if email and senha:
            # Usa o modelo de usuário customizado para autenticação
            user = authenticate(email=email, password=senha)
            if not user:
                raise forms.ValidationError("Email ou senha incorretos.")
        
        return self.cleaned_data
    
class CadastroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'entrada-input input-box',
        'placeholder': 'Digite sua senha',
        'required': True,
        'autocomplete': 'off'
    }))
    confirmar_senha = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'entrada-input input-box',
        'placeholder': 'Confirme sua senha',
        'required': True,
        'autocomplete': 'off'
    }))

    class Meta:
        model = Usuario
        fields = ['nome', 'cpf', 'data_nascimento', 'email', 'role', 'foto']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'entrada-input input-box',
                'placeholder': 'Digite seu nome',
                'required': True
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'entrada-input input-box',
                'placeholder': 'Digite seu CPF',
                'required': True
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'entrada-input input-box',
                'placeholder': 'Digite sua data de nascimento',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'entrada-input input-box',
                'placeholder': 'Digite seu email',
                'required': True
            }),
            'role': forms.Select(attrs={
                'class': 'entrada-input input-box',
                'required': True
            }),
            'foto': forms.FileInput(attrs={
                'class': 'entrada-input input-box',
                'required': False
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError("As senhas não coincidem.")

        return cleaned_data