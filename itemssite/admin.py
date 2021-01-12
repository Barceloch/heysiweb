# -*- coding: utf-8 -*-
from django.contrib import admin
from itemssite.models import BannerSlider, HomePost, HomeService, Faq
from django import forms

class BannerSlider_Admin(admin.ModelAdmin):
    #change_form_template = 'admin/change_form.html'
    pass
    list_display = ('title','slug', 'slider_img')
    list_filter = ['title']
    search_fields = ['title', 'slug']
    prepopulated_fields = { 'slug' : ('title', ) }
            
class HomePost_Admin(admin.ModelAdmin):
    change_form_template = 'change_form/admin/change_form.html'
    #form = HomePost_AdminForm
    pass
    list_display = ('title','description', 'language', 'home_img')
    list_filter = ['title', 'language']
    search_fields = ['title', 'language']
    
class HomeService_Admin(admin.ModelAdmin):
    #change_form_template = 'admin/change_form.html'
    pass
    list_display = ('title','description', 'language')
    list_filter = ['title', 'language']
    search_fields = ['title', 'language']

class Faq_Admin(admin.ModelAdmin):
    #change_form_template = 'admin/change_form.html'
    #form = HomePost_AdminForm
    pass
    list_display = ('question','language')
    list_filter = ['question', 'language']
    search_fields = ['tquestion', 'language']

admin.site.register(Faq, Faq_Admin)
admin.site.register(BannerSlider, BannerSlider_Admin)
admin.site.register(HomePost, HomePost_Admin)
admin.site.register(HomeService, HomeService_Admin)
