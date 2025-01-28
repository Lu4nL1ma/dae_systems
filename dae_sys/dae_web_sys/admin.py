from django.contrib import admin
from dae_web_sys import models


@admin.register(models.regiao)
class regiao(admin.ModelAdmin):
    list_display = 'id','regiao',

# Register your models here.
