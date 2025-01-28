from django.db import models

# Create your models here.

class regiao_municipio(models.Model):
    regiao = models.CharField(max_length=40, default='')
    municipio = models.CharField(max_length=40, default='')
    def __str__(self) -> str:
        return self.regiao_municipio
    
class regiao(models.Model):
    regiao = models.CharField(max_length=40, default='')
    def __str__(self) -> str:
        return self.regiao