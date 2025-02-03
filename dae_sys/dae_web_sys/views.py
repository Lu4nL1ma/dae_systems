from django.shortcuts import render
from dae_web_sys.models import regiao, regiao_municipio, custos
from datetime import datetime
from django.urls import reverse
import pandas as pd

# Create your views here.

def home(request):

        var = ''
        
        ano_atual = datetime.now().year
        
        anos = [(str(ano)) for ano in range(2020, ano_atual + 5)]
        
        reg = regiao.objects.all()
        
        munis = regiao_municipio.objects.all()
        
        context = {'r': reg, 'anos': anos,'m': munis, 'servi': ['Internet', 'Link de Dados', 'Internet + Link de Dados'], 'var': var}
        
        return render(request, "index.html", context)

def home_filtrada(request, r_regiao):

        var = r_regiao
        
        ano_atual = datetime.now().year
        
        anos = [(str(ano)) for ano in range(2020, ano_atual + 5)]
        
        reg = regiao.objects.all()
        
        munis = regiao_municipio.objects.filter(regiao=r_regiao)
        
        context = {'r': reg, 'anos': anos,'m': munis, 'servi': ['Internet', 'Link de Dados', 'Internet + Link de Dados'], 'var': var}
        
        return render(request, "index.html", context)

def cust_muni(request):

        if request.method == 'POST':

                #pegando os dados

                muni = request.POST.get('muni')

                mb_link = request.POST.get('mb_link')

                mb_net = request.POST.get('mb_net')

                print(f'DADOS: {mb_link}')

                print(f'NET: {mb_net}')

                qry = custos.objects.all()

                df = pd.DataFrame(list(qry.values()))

                def cal_pref(row):
                        
                        somar =  float((row['cunittransp']) + float(row['cmanut'])) / (float(1) - 0.1 - 0.2 - 0.1704)

                        somar = round(somar, 2)

                        return somar
                
                def atualizar(row):
                        
                        row['cunittransp'] = float((row['cunittransp'])) * int(mb_link)

                        atuali = round(row['cunittransp'], 2)

                        return atuali
                
                def atualizar_mbps(row):

                        row['mbps'] = mb_link

                        atuali = row['mbps']
                        
                        return atuali
                
                #aplicando mudanças no df

                if mb_net != None:

                        df['mbps'] = df.apply(atualizar_mbps, axis=1)

                        df['cunittransp'] = df.apply(atualizar, axis=1)

                        df['preco_final'] = df.apply(cal_pref, axis=1)

                        df = df[df['municipio'] == muni ]

                        context = {'df': df}

                        return render(request, "resultado.html", context)
                
                else:
                        df['preco_final'] = df.apply(cal_pref, axis=1)

                        df = df[df['municipio'] == muni ]

                        context = {'df': df}

                        return render(request, "resultado.html", context)

