# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'HomePost.details'
        db.alter_column('itemssite_homepost', 'details', self.gf('tinymce.models.HTMLField')())

    def backwards(self, orm):

        # Changing field 'HomePost.details'
        db.alter_column('itemssite_homepost', 'details', self.gf('django.db.models.fields.TextField')())

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
            'details': ('tinymce.models.HTMLField', [], {}),
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