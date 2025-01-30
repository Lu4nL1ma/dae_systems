from django.shortcuts import render
from dae_web_sys.models import regiao, regiao_municipio, custos
from datetime import datetime
from django.urls import reverse
import pandas as pd

# Create your views here.

def home(request):
        
        ano_atual = datetime.now().year
        
        anos = [(str(ano)) for ano in range(2020, ano_atual + 5)]
        
        reg = regiao.objects.all()
        
        munis = regiao_municipio.objects.all()

        for i in reg:
                teste = i.id
        
        context = {'r': reg, 'anos': anos,'m': munis, 'teste': teste}
        
        return render(request, "index.html", context)

def home_filtrada(request, r_regiao):
        
        ano_atual = datetime.now().year
        
        anos = [(str(ano)) for ano in range(2020, ano_atual + 5)]
        
        reg = regiao.objects.all()
        
        munis = regiao_municipio.objects.filter(regiao=r_regiao)
        
        context = {'r': reg, 'anos': anos,'m': munis}
        
        return render(request, "index.html", context)

def cust_muni(request):

        muni = request.POST.get('muni')

        qry = custos.objects.all()

        df = pd.DataFrame(list(qry.values()))

        def cal_pref(row):
                
                somar = ( float((row['cunittransp']) * float(row['mbps']) ) + float(row['cmanut'])) / (float(1) - 0.1 - 0.2 - 0.1704)

                somar = round(somar, 2)

                return somar

        df['preco_final'] = df.apply(cal_pref, axis=1)

        df_filtrado = df[df['municipio'] == muni ]

        context = {'df': df_filtrado}

        return render(request, "resultado.html", context)
