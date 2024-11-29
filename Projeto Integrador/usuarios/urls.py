from django.urls import path
from .views import login_view, logout_view, recuperar_senha, cadastro_view

app_name = 'usuarios'

urlpatterns = [
    path('', login_view, name='login'),  # Define a página de login como a página principal
    path('logout/', logout_view, name='logout'),
    path('recuperar-senha/', recuperar_senha, name='recuperar_senha'),  # Adiciona a rota para recuperar senha
    path('cadastro/', cadastro_view, name='cadastro'),  # Adiciona a rota para cadastro
]