from django.contrib import admin
from dae_web_sys import models


@admin.register(models.regiao)
class regiao(admin.ModelAdmin):
    list_display = 'id','regiao'
    class Meta:
        verbose_name = "Regiõe"

@admin.register(models.regiao_municipio)
class regiao_municipio(admin.ModelAdmin):
    list_display = 'id', 'meso','regiao', 'municipio'
    class Meta:
        verbose_name = "Município"

@admin.register(models.custos)
class custos(admin.ModelAdmin):
    list_display = 'id', 'mesorreg' , 'regint' , 'municipio', 'modalidade', 'tecnologia','cunittransp', 'cmanut'
    class Meta:
        verbose_name = "Custo"

@admin.register(models.reajuste)
class reajuste(admin.ModelAdmin):
    list_display = 'id','ano', 'indice' 
    class Meta:
        verbose_name = "Custo"

@admin.register(models.mesorregiao)
class mesorregiao(admin.ModelAdmin):
    list_display = 'id','mesorregiao' 
    class Meta:
        verbose_name = "Mesorregiõe"