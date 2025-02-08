def cal_pref(row):
    somar =  float((row['cunittransp']) + float(row['cmanut'])) / (float(1) - 0.1 - 0.2 - 0.1704)

    somar = round(somar, 2)

    return somar
                
def atualizar(row, mb_link):
                        
    row['cunittransp'] = float((row['cunittransp'])) * int(mb_link)

    atuali = round(row['cunittransp'], 2)

    return atuali
                
def atualizar_mbps(row, mb_link):

    row['mbps'] = mb_link

    atuali = row['mbps']
                        
    return atuali