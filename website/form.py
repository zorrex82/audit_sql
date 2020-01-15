from django import forms


class NameForm(forms.Form):
    login = forms.CharField(label='Usuário', max_length=100)
    password = forms.CharField(label='Senha', max_length=100)

