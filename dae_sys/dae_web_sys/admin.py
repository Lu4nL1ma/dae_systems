from django.contrib import admin
from dae_web_sys import models


@admin.register(models.regiao)
class regiao(admin.ModelAdmin):
    list_display = 'id','regiao',

@admin.register(models.regiao)
class regiao_municipio(admin.ModelAdmin):
    list_display = 'id', 'municpio','regiao',

@admin.register(models.regiao)
class custos(admin.ModelAdmin):
    list_display = 'id', 'mesorreg' , 'regint' , 'municpio', 'modalidade', 'tecnologia','cunittransp', 'cmanut',
