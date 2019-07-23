from django import forms


class DiagnosticoForm1(forms.Form):
    tipo_empresa = forms.ChoiceField(choices=(('b2c', 'B2C'), ('b2b', 'B2B')), required=True)
    qtd_venda = forms.IntegerField(label='Quantidade de vendas', required=True)
