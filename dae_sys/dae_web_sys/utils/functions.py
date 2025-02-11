import locale
from dae_web_sys.models import reajuste

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Exemplo: Brasi

def cal_pref(row):
    somar =  float((row['cunittransp']) + float(row['cmanut'])) / (float(1) - 0.1 - 0.2 - 0.1704)

    somar = round(somar, 2)

    return somar
    
                
def formata_reais(valor):

    return locale.currency(valor, grouping=True)


def updt_valor(valor, a):
  ajustes = reajuste.objects.values_list('indice', flat=True)
  ano = a - 2021
  
  for i in range(ano):
    
    valor

    calculo = float(valor) * (1 + ( float(ajustes[i]) / 100 ))

    valor = calculo

  return round(valor,2)

def atuali_transp(row, mb_link):
   
   mb_link = int(mb_link)

   if mb_link <= 10:
      
      result = float(row) * float(mb_link)

      return round(result,2)
      
   
   elif mb_link > 10 and mb_link <= 20:
   
      mb_link = mb_link * 0.9803
      
      row = float(mb_link) * float(row)
      
      result = row

      return round(result,2)
   
   elif mb_link > 20 and mb_link <= 40:
      
        mb_link = mb_link * 0.9606
        
        row = float(mb_link) * float(row)
        
        result = row

        return round(result,2)
   
   elif mb_link > 40 and mb_link <= 80:
      
        mb_link = mb_link * 0.9417
        
        row = float(mb_link) * float(row)
        
        result = row

        return round(result,2)
   
   elif mb_link > 80 and mb_link <= 160:
      
        mb_link = mb_link * 0.9228
        
        row = float(mb_link) * float(row)
        
        result = row

        return round(result,2)
   
   elif mb_link > 160 and mb_link <= 320:
      
        mb_link = mb_link * 0.9047
        
        row = float(mb_link) * float(row)
        
        result = row

        return round(result,2)
   
   elif mb_link > 320 and mb_link <= 640:
      
        mb_link = mb_link * 0.8866
        
        row = float(mb_link) * float(row)
        
        result = row

        return round(result,2)
   
   elif mb_link > 640 and mb_link <= 1280:
      
        mb_link = mb_link * 0.8685
        
        row = float(mb_link) * float(row)
        
        result = row

        return round(result,2)
   
   elif mb_link > 1280 and mb_link <= 2560:
      
        mb_link = mb_link * 0.8512
        
        row = float(mb_link) * float(row)
        
        result = row

        return round(result,2)
   
   elif mb_link > 2560 and mb_link <= 5120:
      
        mb_link = mb_link * 0.8339
        
        row = float(mb_link) * float(row)
        
        result = row

        return round(result,2)
   
   elif mb_link > 5120 and mb_link <= 10240:
      
        mb_link = mb_link * 0.8173
        
        row = float(mb_link) * float(row)
        
        result = row

        return round(result,2)
        


      
