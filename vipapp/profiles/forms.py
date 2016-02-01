# coding: utf-8
from django import forms
from django.contrib.auth.models import Group
from pinax.referrals.models import Referral
from .models import Order, Ticket

class SignupForm(forms.Form):
    pass

    def signup(self, request, user):
        group = 'advertiser'
        g = Group.objects.get(name=group)
        user.groups.add(g)
        referral = Referral.create(user=user, redirect_to="index")
        user.referral = referral
        user.save()

class CreateOrder(forms.ModelForm):
    app_name = forms.CharField(label='Название приложения', max_length=128, widget=forms.TextInput(attrs={'class': "form-control"}))  
    id_apps = forms.CharField(label='ID приложения', max_length=128, widget=forms.TextInput(attrs={'class': "form-control"}))
    link_redirect = forms.CharField(label='Ссылка для переадресации', max_length=128, widget=forms.TextInput(attrs={'class': "form-control"}))
    order_description = forms.CharField(label='Описание заказа', max_length=128, widget=forms.Textarea(attrs={'class': "form-control"}))


    class Meta:
        model = Order
        exclude = ['user', 'status']

class CreateSupport(forms.ModelForm):
    title =  forms.CharField(label='Заголовок', max_length=128, widget=forms.TextInput(attrs={'class': "form-control"}))
    text = forms.CharField(label='Текст', max_length=500, widget=forms.Textarea(attrs={'class': "form-control"}))

   

 
    class Meta:
        model = Ticket
        exclude = ['user', 'closed']
