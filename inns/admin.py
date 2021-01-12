# -*- coding: utf-8 -*-
from inns.models import Inn, Image, Album, Comment, BookRoom, ReservationKey
from django.contrib import admin
from django import forms


class Comment_Admin(admin.ModelAdmin):
    pass
    list_display = ('inn', 'name', 'email', 'text')
    list_filter = ['name', 'email']
    search_fields = ['inn']


class Inn_Admin(admin.ModelAdmin):
    change_form_template = 'change_form/admin/change_form.html'
    pass
    list_display = ('name', 'inn_img', 'machine_name', 'rooms', 'high_season', 'is_premium', 'is_public')
    list_filter = ['rooms']
    search_fields = ['name']
    prepopulated_fields = { 'machine_name' : ('name', ) }

class ImageAdminInline(admin.StackedInline):
      model = Image
      extra = 3


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['album_name']}),
    ]
    inlines = [ImageAdminInline]
    list_display = ["album_name"]

class BookRoom_Admin(admin.ModelAdmin):
    pass
    list_display = ('name', 'email', 'country', 'date_in', 'date_out', 'paxs', 'rooms', 'inn', 'is_confirmed', 'created_on')
    list_filter = ['name','country']
    search_fields = ['name', 'email', 'country']

class ReservationKey_Admin(admin.ModelAdmin):
    pass
    list_display = ('book', 'inn_key', 'i_confirmed', 'client_key', 'c_confirmed')
    list_filter = ['book']
    search_fields = ['book']

admin.site.register(ReservationKey, ReservationKey_Admin)
admin.site.register(BookRoom, BookRoom_Admin)
admin.site.register(Inn, Inn_Admin)
admin.site.register(Comment, Comment_Admin)
admin.site.register(Album, AlbumAdmin)




