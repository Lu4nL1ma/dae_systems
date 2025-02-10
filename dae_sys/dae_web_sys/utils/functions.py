import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Exemplo: Brasi

def cal_pref(row):
    somar =  float((row['cunittransp']) + float(row['cmanut'])) / (float(1) - 0.1 - 0.2 - 0.1704)

    somar = round(somar, 2)

    return somar
                
def formata_reais(valor):
    return locale.currency(valor, grouping=True)