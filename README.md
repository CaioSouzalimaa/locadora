# API para uma Locadora de Filmes

Este projeto consiste em criar uma API que atenda as funcionalidades de uma locadora de filmes.

# Configurando o ambiente
Para este projeto criamos um ambiente virtual e utilizamos o **django** em conjunto com **rest_framework**.

Logo abaixo temos os passos dessa configuração.

```bash
-> python -m venv venv #Criamos um ambiente virtual nomeado de venv
-> ./venv/Scripts/activate #Ativamos o ambiente virtual 
-> pip install django djangorestframework #Instalamos as dependências do projeto
```

Após isso temos que criar o projeto e seus apps

```bash
-> django-admin startproject locadora . #Criação do projeto OBS:(O ponto server para indicar o diretório atual)
-> django-admin startapp filmes #Criação do app
```
# Criação do modelo e API
Precisamos dizer ao projeto que criamos o app filmes e estamos utilizando o rest_framework, isso é feito no arquivo settings.py localizado em /locadora/settings.py

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', #informa que estamos utilizando o rest_framework
    'filmes', #informa a criação  do app filmes
]
```

Agora vamos criar o modelo onde definiremos os campos que serão utilizados, esse arquivo está em /locadora/filmes/models.py

```py
from django.db import models
from uuid import uuid4

class Filmes(models.Model):
    #Definindo os atributos dos campos
    id_filme = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_filme = models.CharField(max_length=255)
    nome_cliente = models.CharField(max_length=255)
    dia_alugado = models.DateField(auto_now_add=True)
    dia_devolver = models.DateField()
    valor = models.FloatField()

```
# Serializers e Views
Em /locadora/filmes criamos a pasta /api e dentro dela os arquivos viewsets.py e serializers.py

### Serializers:
```py
from rest_framework import serializers
from filmes import models

class FilmesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Filmes
        fields = '__all__' #todos os campos presentes no model
```

### Viewsets:
```py
from rest_framework import viewsets
from filmes.api import serializers
from filmes import models

class FilmesView(viewsets.ModelViewSet):
    serializer_class = serializers.FilmesSerializer
    queryset = models.Filmes.objects.all() #todos os campos presentes no model
```

# Configurando as rotas
Agora só falta configurarmos as rotas.
```py
from django.contrib import admin
from django.urls import path, include #Adicionamos o include

from rest_framework import routers 
from filmes.api import viewsets as FilmesViewSets 

#objeto de rota
route = routers.DefaultRouter()
route.register(r'Filmes',FilmesViewSets.FilmesView, basename= "Filmes")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)), 
]

```
Antes de executarmos o servidor precisamos avisar sobre a criação dos modelos e fazer a migração dessas informações para o banco de dados.

```bash
-> python manage.py makemigrations #Informamos as mudanças no modelo
-> python manage.py migrate #Migramos essas informações para o banco
-> python manage.py runserver #Inicia o servidor
```
