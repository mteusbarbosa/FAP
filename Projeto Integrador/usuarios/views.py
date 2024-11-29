from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, CadastroForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            
            # Autentica o usuário
            user = authenticate(request, email=email, password=senha)
            
            if user is not None:
                login(request, user)
                return redirect('processos:lista_processos')  # Redireciona para lista de processos
            else:
                messages.error(request, 'Email ou senha incorretos.')
    else:
        form = LoginForm()
    
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('usuarios:login')

def recuperar_senha(request):
    return render(request, 'usuarios/recuperar_senha.html')

def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['senha'])
            usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('usuarios:login')
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        form = CadastroForm()
    
    return render(request, 'usuarios/cadastro.html', {'form': form})