# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BannerSlider'
        db.create_table('itemssite_bannerslider', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, primary_key=True)),
            ('details', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('slider_img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('itemssite', ['BannerSlider'])

        # Adding model 'HomePost'
        db.create_table('itemssite_homepost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('details', self.gf('django.db.models.fields.TextField')()),
            ('home_img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(default='es', max_length=2)),
        ))
        db.send_create_signal('itemssite', ['HomePost'])

        # Adding model 'HomeService'
        db.create_table('itemssite_homeservice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('details', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('language', self.gf('django.db.models.fields.CharField')(default='es', max_length=2)),
        ))
        db.send_create_signal('itemssite', ['HomeService'])

        # Adding model 'Faq'
        db.create_table('itemssite_faq', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('answer', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('language', self.gf('django.db.models.fields.CharField')(default='es', max_length=2)),
        ))
        db.send_create_signal('itemssite', ['Faq'])


    def backwards(self, orm):
        # Deleting model 'BannerSlider'
        db.delete_table('itemssite_bannerslider')

        # Deleting model 'HomePost'
        db.delete_table('itemssite_homepost')

        # Deleting model 'HomeService'
        db.delete_table('itemssite_homeservice')

        # Deleting model 'Faq'
        db.delete_table('itemssite_faq')


    models = {
        'itemssite.bannerslider': {
            'Meta': {'object_name': 'BannerSlider'},
            'details': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'slider_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'itemssite.faq': {
            'Meta': {'object_name': 'Faq'},
            'answer': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'es'", 'max_length': '2'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'itemssite.homepost': {
            'Meta': {'object_name': 'HomePost'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'details': ('django.db.models.fields.TextField', [], {}),
            'home_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'es'", 'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'itemssite.homeservice': {
            'Meta': {'object_name': 'HomeService'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'details': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'es'", 'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['itemssite']