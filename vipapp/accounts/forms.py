# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from pinax.referrals.models import Referral
from userena.forms import AuthenticationForm, SignupForm
from django.contrib.auth.models import Group
from userena.models import UserenaSignup
from userena import settings as userena_settings



def identification_field_factory(label, error_required):
    attrs_dict = {'class': 'form-control', 'placeholder' : label}
    return forms.CharField(label=label,
                           widget=forms.TextInput(attrs=attrs_dict),
                           max_length=75,
                           error_messages={'required': error_required})

class AuthenticationFormCustom(AuthenticationForm):
    identification = identification_field_factory(_(u"Введите ваш логин"),
                                                  _("Either supply us with your email or username."))

    password = forms.CharField(label=_(u"Введите ваш пароль"),
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder' : u'Введите ваш пароль'}, render_value=False))


class SignupFormCustom(SignupForm):
     USERNAME_RE = r'^[\.\w]+$'
     username = forms.RegexField(regex=USERNAME_RE,
                                max_length=30,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Логин'}), label=_("Username"))
     attrs_dict = {'class': 'form-control', 'placeholder' : 'Введите ваш email'}
     email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict, maxlength=75)), label=_("Email"))     

     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder' : 'Введите ваш пароль'}, render_value=False),
                                label=_("Create password"))
     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder' : 'Введите ваш пароль еще раз'}, render_value=False), label=_("Repeat password"))

     def save(self):
         """ Creates a new user and account. Returns the newly created user. """
         username, email, password = (self.cleaned_data['username'],
                                     self.cleaned_data['email'],
                                     self.cleaned_data['password1'])

         new_user = UserenaSignup.objects.create_user(username,
                                                     email,
                                                     password,
                                                     not userena_settings.USERENA_ACTIVATION_REQUIRED,
                                                     userena_settings.USERENA_ACTIVATION_REQUIRED)
        
         group = 'advertiser'
         g = Group.objects.get(name=group)
         new_user.groups.add(g)
         referral = Referral.create(user=new_user, redirect_to="index")
         new_user.referral = referral

         return new_user

