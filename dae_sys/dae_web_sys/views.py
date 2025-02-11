from django.shortcuts import render
from dae_web_sys.models import regiao, regiao_municipio, custos
from datetime import datetime
from django.urls import reverse
from django.http import JsonResponse
from .utils.functions import cal_pref, formata_reais, updt_valor
import pandas as pd

# Create your views here.

def formulario(request):

        var = ''
        
        ano_atual = datetime.now().year
        
        anos = [(str(ano)) for ano in range(2021, ano_atual + 1)]
        
        reg = regiao.objects.all()
        
        munis = regiao_municipio.objects.all()
        
        context = {'regioes': reg, 'anos': anos,'munis': munis, 'servi': ['Internet', 'Link de Dados', 'Internet + Link de Dados'], 'var': var}
        
        return render(request, "index.html", context)

def carregar_municipios(request):

    regiao = request.GET.get('regiao_id')


    municipios = regiao_municipio.objects.filter(regiao=regiao).values('municipio')

    return JsonResponse(list(municipios), safe=False)



def cust_muni(request):

        if request.method == 'POST':

                #pegando os dados

                muni = request.POST.get('municipio')

                mb_link = request.POST.get('mb_link')

                mb_net = request.POST.get('mb_net')

                ano = request.POST.get('ano')

                print(ano)

                qry = custos.objects.all()

                df = pd.DataFrame(list(qry.values()))
                
                #aplicando mudanças no df

                if mb_net != None:

                        df['mbps'] = df['mbps'].map(lambda x: int(mb_link))

                        df['cunittransp'] = df['cunittransp'].map(lambda x: x * int(mb_link))

                        df['preco_final'] = df.apply(cal_pref, axis=1)

                        df = df[df['municipio'] == muni ]

                        df['cunittransp'] = df['cunittransp'].map(formata_reais)

                        df['cmanut'] = df['cmanut'].map(formata_reais)

                        if int(ano) > 2021:
                               
                               df['preco_final'] = df['preco_final'].apply(updt_valor, args=(int(ano),))

                               df['preco_final'] = df['preco_final'].map(formata_reais)

                        else:
                                df['preco_final'] = df['preco_final'].map(formata_reais)

                               
                        context = {'df': df}

                        return render(request, "resultado.html", context)
                
                else:
                        df['preco_final'] = df.apply(cal_pref, axis=1)

                        df = df[df['municipio'] == muni ]

                        context = {'df': df}

                        return render(request, "resultado.html", context)

