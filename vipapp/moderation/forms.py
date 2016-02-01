from django import forms
from profiles.models import Order


class ModeratorForm(forms.ModelForm):
    app_name = forms.CharField(label='Название приложения', max_length=128, widget=forms.TextInput(attrs={'class': "form-control"})) 
    class Meta:
        model = Order
        fields = "__all__" 

