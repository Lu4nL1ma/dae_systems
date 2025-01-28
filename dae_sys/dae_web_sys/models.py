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

class custos(models.Model):
    mesorreg = models.CharField(max_length=40, default='')
    regint = models.CharField(max_length=40, default='')
    municipio = models.CharField(max_length=40, default='')
    modalidade = models.CharField(max_length=40, default='')
    tecnologia = models.CharField(max_length=40, default='')
    mbps = models.CharField(max_length=40, default='')
    cunittransp = models.FloatField(default=0.0)
    cmanut = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.custos