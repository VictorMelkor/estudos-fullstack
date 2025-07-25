"""
📘 INTRODUÇÃO AO DJANGO (Framework Web com Python)

Django é um framework web de alto nível para desenvolvimento rápido e limpo com Python.
Ele segue o padrão MTV (Model-Template-View), que é parecido com o MVC.

✔️ Principais objetivos:
- Automatizar o máximo possível do trabalho repetitivo
- Focar em segurança, escalabilidade e boas práticas
- Tornar fácil criar sites completos com banco de dados, painel admin, rotas e templates

📦 INSTALAÇÃO:
pip install django
"""

# ✅ Criando um projeto Django
# No terminal, usamos:
# django-admin startproject meu_projeto

# Isso cria uma estrutura inicial com arquivos como:
# manage.py, settings.py, urls.py, wsgi.py

"""
📁 Estrutura básica de um projeto:
meu_projeto/
├── manage.py         # utilitário para gerenciar comandos do projeto
└── meu_projeto/      # pasta principal com configurações
    ├── settings.py   # configurações gerais
    ├── urls.py       # rotas do projeto
    ├── wsgi.py       # interface com servidores
"""

# ✅ Criando um app dentro do projeto
# python manage.py startapp cadastro

"""
Cada "app" é um módulo funcional, como: blog, produtos, usuários, etc.
Um projeto Django pode conter vários apps.

cadastro/
├── admin.py       # registro no admin
├── apps.py        # configurações do app
├── models.py      # definição das tabelas (ORM)
├── views.py       # lógica das páginas (controladores)
├── urls.py        # (criado manualmente) rotas específicas do app
├── templates/     # HTML
├── static/        # CSS, JS, imagens
"""

# ✅ Exemplo de MODEL (camada de dados)
# Definimos modelos Python que viram tabelas no banco (ORM)

from django.db import models

class Desenvolvedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    linguagem = models.CharField(max_length=50)
    senioridade = models.CharField(max_length=30)

# Depois, executamos:
# python manage.py makemigrations
# python manage.py migrate
# Isso cria ou atualiza as tabelas no banco de dados

# ✅ Exemplo de VIEW (lógica da aplicação)

from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo ao sistema de cadastro de devs!")

# ✅ Exemplo de URL (rota do site)
# Em urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

# ✅ Exemplo de TEMPLATE (HTML dinâmico)
# Criamos arquivos HTML em /templates

# templates/home.html
"""
<!DOCTYPE html>
<html>
<head><title>Cadastro</title></head>
<body>
  <h1>Bem-vindo, dev!</h1>
</body>
</html>
"""

# Na view, usamos:
# from django.shortcuts import render
# return render(request, 'home.html')

"""
🛠 PRINCIPAIS FUNCIONALIDADES DO DJANGO:
- Rotas e URLs organizadas
- Templates HTML com engine integrada
- ORM completo para banco de dados (sem SQL direto)
- Painel de administração automático
- Formulários com validação
- Suporte a autenticação, permissões e sessões
- Integração com APIs e apps RESTful
"""

# ✅ Rodando o servidor local
# python manage.py runserver
# Acesse http://127.0.0.1:8000

"""
🎯 CONCLUSÃO:
Django é ideal para quem quer construir aplicações web profissionais com rapidez e organização.
Ele cuida de muitos detalhes internos para que você foque na lógica da aplicação.

📌 Dica:
Estude cada parte com calma — comece por models, views e templates.
A documentação oficial é excelente: https://docs.djangoproject.com/pt-br/
"""

