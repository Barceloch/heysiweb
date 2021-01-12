# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label=_('Asunto:'))
    message = forms.CharField(widget=forms.Textarea, label=_('Mensaje:'))
    sender = forms.EmailField(label=_('De: (su Email)'))
    cc_myself = forms.BooleanField(required=False)
    captcha = CaptchaField(help_text=(_(u'Escriba los caracteres de la imágen')))
