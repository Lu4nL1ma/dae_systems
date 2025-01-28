from django import forms
from datetime import datetime
from .models import regiao, regiao_municipio

class simulador(forms.Form):

    ano = forms.ChoiceField(choices=[])

    regiao_de_integração = forms.ChoiceField(choices=regiao.objects.values_list('regiao', 'regiao'))

    município = forms.ModelChoiceField(queryset=regiao_municipio.objects.none())
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ano_atual = datetime.now().year
        anos = [(ano, str(ano)) for ano in range(2020, ano_atual + 5)]
        self.fields['ano'].choices = anos
