from django import forms


class HostCheckForm(forms.Form):
    ip = forms.CharField()
