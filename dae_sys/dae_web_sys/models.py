from django.db import models

# Create your models here.
    
class regiao(models.Model):
    regiao = models.CharField(max_length=40, default='')
    class Meta:
        verbose_name = 'Regiõe'


class regiao_municipio(models.Model):
    regiao = models.CharField(max_length=40, default='')
    municipio = models.CharField(max_length=40, default='')
    
    class Meta:
        verbose_name = 'Município'


class custos(models.Model):
    mesorreg = models.CharField(max_length=40, default='')
    regint = models.CharField(max_length=40, default='')
    municipio = models.CharField(max_length=40, default='')
    modalidade = models.CharField(max_length=40, default='')
    tecnologia = models.CharField(max_length=40, default='')
    mbps = models.CharField(max_length=40, default='')
    cunittransp = models.FloatField(default=0.0)
    cmanut = models.FloatField(default=0.0)
    class Meta:
        verbose_name = 'Custos dos Serviço'

class reajuste(models.Model):
    ano = models.CharField(max_length=40, default='')
    indice = models.FloatField(default=0.0)
    class Meta:
        verbose_name = 'Reajuste'

class mesorregiao(models.Model):
    mesorregiao = models.CharField(max_length=40, default='')
    class Meta:
        verbose_name = 'Mesorregiõe'
