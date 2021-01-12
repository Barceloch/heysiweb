# -*- coding: utf-8 -*-
from django.db import models
from heysiweb.settings import STATIC_URL, LANGUAGES
from django.core.files import File
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from tempfile import *
import datetime

##Modelo para los  Album
class Album(models.Model):
    album_name = models.CharField(default = u'Galería - ', max_length=60, verbose_name=_(u'Nombre'))

    class Meta:
		 verbose_name = _(u'Galería de fotos')
		 verbose_name_plural = _(u'Galerías de fotos')

    def __unicode__(self):
        return self.album_name

##Modelo para las Imagenes
class Image(models.Model):
    album = models.ForeignKey(Album, null=True, blank=True)
    title = models.CharField(max_length=60, blank=True, null=True, verbose_name=_(u'Nombre'))
    description = models.CharField(max_length=50,verbose_name=_(u'Descripción'))
    image = ThumbnailerImageField(upload_to="images/album_img/", null=False, blank=False,
                                      resize_source=dict(size=(600, 300), sharpen=True), verbose_name=_(u'Imágen'))

    class Meta:
		 verbose_name = _(u'Imágen')
		 verbose_name_plural = _(u'Imágenes')

    def __unicode__(self):
        return self.image.name



##Modelo para los Servicios
class Inn(models.Model):
     name = models.CharField(default = u'Hostal - ', max_length=30, null=False, blank=False, verbose_name=_(u'Nombre del Hostal'))
     owner = models.CharField(max_length=30, null=False, blank=False, verbose_name=_(u'Dueño'))
     address = models.CharField(max_length=100, null=False, blank=False, verbose_name=_(u'Dirección'))
     map_img = ThumbnailerImageField(upload_to="images/maps_img/", null=True, blank=True,
                                      resize_source=dict(size=(500, 300), sharpen=True), verbose_name=_(u'Mapa'))
     phone = models.CharField(default = u'(01-41) ', max_length=30, null=False, blank=False, verbose_name=_(u'Teléfono'))
     movil = models.CharField(default = u'(+53) ', max_length=30, null=False, blank=False, verbose_name=_(u'Movil'))
     email = models.EmailField(max_length=75, null=True, blank=True, verbose_name=_(u'E-mail'))     
     machine_name = models.SlugField(max_length=30, primary_key=True, verbose_name=_(u'Link')) 
     rooms = models.PositiveIntegerField(default=1, verbose_name=_(u'Cantidad de habitaciones')) 
     high_season = models.BooleanField(default=True, null=False, blank=False, verbose_name=_(u'Temporada de alsa'))
     min_price = models.DecimalField(default = 20, max_digits=5, decimal_places=2, null=True, blank=True, verbose_name=_(u'Precio en baja')) 
     max_price = models.DecimalField(default = 25, max_digits=5, decimal_places=2, null=True, blank=True, verbose_name=_(u'Precio en alsa'))   
     inn_img = ThumbnailerImageField(upload_to="images/inns_img/", null=False, blank=False,
                                      resize_source=dict(size=(500, 300), sharpen=True), verbose_name=_(u'Imágen'))
     details = models.TextField(null=False, blank=False, verbose_name=_(u'Detalles'))    
     album = models.ForeignKey(Album, null=True, blank=True, verbose_name=_(u'Galería de fotos'))     
     is_premium = models.BooleanField(default=False, null=False, blank=False, verbose_name=_(u'Es premium'))
     is_public = models.BooleanField(default=False, null=False, blank=False, verbose_name=_(u'Publicar'))

     class Meta:
		 verbose_name = _(u'Hostal')
		 verbose_name_plural = _(u'Hostales')

     def __unicode__(self):
        return self.name

#Comentarios
class Comment(models.Model):
    name = models.CharField(max_length=42, verbose_name=_(u'Nombre'))
    email = models.EmailField(max_length=75, verbose_name=_(u'E-mail'))
    country = models.CharField(max_length=200, null=True, blank=True, verbose_name=_(u'País'))
    text = models.TextField(max_length=500, verbose_name=_(u'Comentario'))
    inn = models.ForeignKey(Inn, verbose_name=_(u'Hostal'))
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=_(u'Fecha'))
    is_public = models.BooleanField(default=False, null=False, blank=False, verbose_name=_(u'Publicar'))

    class Meta:
		 verbose_name = _(u'Comentario')

    def __unicode__(self):
        return self.text

#Reservacion de habitaciones
class BookRoom(models.Model):
    name = models.CharField(max_length=42, verbose_name=_(u'Nombre'))
    email = models.EmailField(max_length=75, verbose_name=_(u'E-mail'))
    country = models.CharField(max_length=200, null=False, blank=False, verbose_name=_(u'País'))
    date_in = models.DateField(default=datetime.date.today, verbose_name=_(u'Fecha de llegada'))
    date_out = models.DateField(default=datetime.date.today, verbose_name=_(u'Fecha de salida'))
    paxs = models.PositiveIntegerField(default=2, verbose_name=_(u'Personas'))
    rooms = models.PositiveIntegerField(default=1, verbose_name=_(u'Habitaciones'))
    text = models.TextField(max_length=500, verbose_name=_(u'Mensaje'))
    inn = models.ForeignKey(Inn, verbose_name=_(u'Hostal'))
    is_confirmed = models.BooleanField(default=False, null=False, blank=False, verbose_name=_(u'Confirmada'))    
    is_public = models.BooleanField(default=False, null=False, blank=False, verbose_name=_(u'Publicar'))
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=_(u'Fecha'))
    
    class Meta:
		 verbose_name = _(u'Reservación')
		 verbose_name_plural = _(u'Reservaciones')

    def __unicode__(self):
        return self.name

class ReservationKey(models.Model):
     inn_key = models.CharField(max_length=40, verbose_name=_(u'Código del hostal'))
     i_confirmed = models.BooleanField(default=False, null=False, blank=False, verbose_name=_(u'El hostal ha confirmado'))
     client_key = models.CharField(max_length=40, verbose_name=_(u'Código del Cliente'))
     c_confirmed = models.BooleanField(default=False, null=False, blank=False, verbose_name=_(u'El cliente ha confirmado'))
     book = models.ForeignKey(BookRoom, null=False, blank=False, verbose_name=_(u'Reservación'))

     class Meta:
		 verbose_name = _(u'Código de reservación')
		 verbose_name_plural = _(u'Códigos de reservaciones')

     def __unicode__(self):
         return self.inn_key



