# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from inns.models import Inn, Comment, BookRoom, ReservationKey
from captcha.fields import CaptchaField
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import AdminDateWidget

class Add_InnForm(ModelForm):
     class Meta:
         model = Inn
         exclude = ['machine_name', 'album', 'map_img', 'is_premium', 'is_public']

class CommentForm(forms.ModelForm):
    captcha = CaptchaField(help_text=(_(u'Escriba los caracteres de la imágen')))
    class Meta:
        model = Comment
        exclude = ['inn', 'created_on', 'is_public']

class ReservationForm(forms.ModelForm):
    captcha = CaptchaField(help_text=(_(u'Escriba los caracteres de la imágen')))
    class Meta:
        model = BookRoom
        exclude = ['inn', 'is_confirmed', 'created_on', 'is_public']

class InnConfirmForm(forms.Form):
    key_inn = forms.CharField(label=_(u'Código del hostal:'), error_messages={'required': _(u'Debe ingresar el código de confirmación')})

    def clean_key_service(self):
        data = self.cleaned_data['key_inn']
        if not ReservationKey.objects.filter(service_key__icontains=data):
            raise forms.ValidationError(_(u'El código es incorrecto'))
        return data

class ClientConfirmForm(forms.Form):
    key_client = forms.CharField(label=_(u'Código del cliente:'), error_messages={'required': _(u'Debe ingresar el codigo de confirmación')})


    def clean_key_client(self):
        data = self.cleaned_data['key_client']
        if not ReservationKey.objects.filter(client_key__icontains=data):
            raise forms.ValidationError(_(u'El código es incorrecto'))
        return data
