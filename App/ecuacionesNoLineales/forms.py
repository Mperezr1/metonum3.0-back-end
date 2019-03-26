from django import forms


class EcuacionesNoLinealesForms(forms.Form):
    funcion = forms.CharField()
    valorInicial = forms.IntegerField()
    delta = forms.IntegerField()
    iter = forms.IntegerField()
