"""
URL configuration for dae_sys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dae_web_sys import views

urlpatterns = [
    path('', views.formulario, name='form'),
    path('admin/', admin.site.urls),
    path('custos/', views.cust_muni, name='custos'),
    path('carregar_por_regiao/', views.carregar_por_regiao, name='reg_fil'),
   path('carregar_por_mesorregiao/', views.carregar_por_mesorregiao, name='mes_fil')
    
]
