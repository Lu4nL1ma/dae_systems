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

def custos(request):

        custos = custos.objects.all()

        df = pd.DataFrame(list(custos.values()))

        df['preço_final'] = 1000

        conn.close()

        context = {'df': df}

        return render(request, "resultado.html", context)
