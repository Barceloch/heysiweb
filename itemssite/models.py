# -*- coding: utf-8 -*-
from django.db import models
from heysiweb.settings import STATIC_URL, LANGUAGES
from easy_thumbnails.fields import ThumbnailerImageField
from django.utils.translation import ugettext_lazy as _

class BannerSlider(models.Model):
   title = models.CharField(max_length=100, verbose_name=_(u'Título'))
   slug = models.SlugField(max_length=255, primary_key=True, verbose_name=_(u'Link'))
   details = models.TextField(max_length=255, verbose_name=_(u'Detalles'))
   slider_img = ThumbnailerImageField(upload_to="images/banner_img/",
                                      null=False, blank=False, verbose_name=_(u'Imágen'))

   class Meta:
		 verbose_name = _(u'Objeto del banner')
		 verbose_name_plural = _(u'Objetos del banner')

   def __unicode__(self):
        return self.title

class HomePost(models.Model):
   title = models.CharField(max_length=100, verbose_name=_(u'Título'))
   description = models.CharField(max_length=255, verbose_name=_(u'Descrition'))
   details = models.TextField(verbose_name=_(u'Detalles'))
   home_img = ThumbnailerImageField(upload_to="images/home_img/", null=True, blank=True, verbose_name=_(u'Imágen'))
   language = models.CharField(max_length=2,choices=LANGUAGES,default='es', verbose_name=_(u'Idioma'))

   class Meta:
		 verbose_name = _(u'Post de inicio')
		 verbose_name_plural = _(u'Posts de inicio')

   def __unicode__(self):
        return self.title

class HomeService(models.Model):
   title = models.CharField(max_length=100, verbose_name=_(u'Título'))
   description = models.CharField(max_length=255, verbose_name=_(u'Detalles'))
   details = models.TextField(max_length=500, verbose_name=_(u'Detalles'))
   language = models.CharField(max_length=2,choices=LANGUAGES,default='es', verbose_name=_(u'Idioma'))


   class Meta:
		 verbose_name = _(u'Servicio HeySi')
		 verbose_name_plural = _(u'Servicios HeySi')

   def __unicode__(self):
        return self.title

class Faq(models.Model):
   question = models.CharField(max_length=255, verbose_name=_(u'Pregunta'))
   answer = models.TextField(max_length=255, verbose_name=_(u'Respuesta'))
   language = models.CharField(max_length=2,choices=LANGUAGES,default='es', verbose_name=_(u'Idioma'))


   class Meta:
		 verbose_name = _(u'Pregunta frecuente')
		 verbose_name_plural = _(u'Preguntas frecuentes')

   def __unicode__(self):
        return self.question
