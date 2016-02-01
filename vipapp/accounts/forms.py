# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from userena.forms import AuthenticationForm



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
