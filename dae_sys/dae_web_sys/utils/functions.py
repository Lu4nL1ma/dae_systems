import locale
from dae_web_sys.models import reajuste

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Exemplo: Brasi

def cal_pref(row):
    somar =  float((row['cunittransp']) + float(row['cmanut'])) / (float(1) - 0.1 - 0.2 - 0.1704)

    somar = round(somar, 2)

    return somar
                
def formata_reais(valor):
    return locale.currency(valor, grouping=True)


def reajuste(valor):
  ajustes = reajuste.objects.values_list('indice', flat=True)
  ajustes = list(ajustes)
  ano = 2023 - 2021
  for i in range(ano):
    valor   
    calculo = valor * (1 + ajustes[i])
    valor = calculo
  return round(valor,2)

