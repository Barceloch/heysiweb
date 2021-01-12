# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table('inns_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album_name', self.gf('django.db.models.fields.CharField')(default=u'Galer\xeda - ', max_length=60)),
        ))
        db.send_create_signal('inns', ['Album'])

        # Adding model 'Image'
        db.create_table('inns_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inns.Album'], null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('inns', ['Image'])

        # Adding model 'Inn'
        db.create_table('inns_inn', (
            ('name', self.gf('django.db.models.fields.CharField')(default=u'Hostal - ', max_length=30)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('map_img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(default=u'(01-41) ', max_length=30)),
            ('movil', self.gf('django.db.models.fields.CharField')(default=u'(+53) ', max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('machine_name', self.gf('django.db.models.fields.SlugField')(max_length=30, primary_key=True)),
            ('rooms', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('high_season', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('min_price', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, default=20.0, max_length=50, max_digits=3, blank=True, null=True)),
            ('max_price', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, default=25.0, max_length=50, max_digits=3, blank=True, null=True)),
            ('inn_img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('details', self.gf('django.db.models.fields.TextField')()),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inns.Album'], null=True, blank=True)),
            ('is_premium', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('inns', ['Inn'])

        # Adding model 'Comment'
        db.create_table('inns_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=42)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('inn', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inns.Inn'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('inns', ['Comment'])

        # Adding model 'BookRoom'
        db.create_table('inns_bookroom', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=42)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_in', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('date_out', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('paxs', self.gf('django.db.models.fields.PositiveIntegerField')(default=2)),
            ('rooms', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('inn', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inns.Inn'])),
            ('is_confirmed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('inns', ['BookRoom'])

        # Adding model 'ReservationKey'
        db.create_table('inns_reservationkey', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('inn_key', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('i_confirmed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('client_key', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('c_confirmed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inns.BookRoom'])),
        ))
        db.send_create_signal('inns', ['ReservationKey'])


    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table('inns_album')

        # Deleting model 'Image'
        db.delete_table('inns_image')

        # Deleting model 'Inn'
        db.delete_table('inns_inn')

        # Deleting model 'Comment'
        db.delete_table('inns_comment')

        # Deleting model 'BookRoom'
        db.delete_table('inns_bookroom')

        # Deleting model 'ReservationKey'
        db.delete_table('inns_reservationkey')


    models = {
        'inns.album': {
            'Meta': {'object_name': 'Album'},
            'album_name': ('django.db.models.fields.CharField', [], {'default': "u'Galer\\xeda - '", 'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'inns.bookroom': {
            'Meta': {'object_name': 'BookRoom'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_in': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'date_out': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inn': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inns.Inn']"}),
            'is_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '42'}),
            'paxs': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2'}),
            'rooms': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '500'})
        },
        'inns.comment': {
            'Meta': {'object_name': 'Comment'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inn': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inns.Inn']"}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '42'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '500'})
        },
        'inns.image': {
            'Meta': {'object_name': 'Image'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inns.Album']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
        },
        'inns.inn': {
            'Meta': {'object_name': 'Inn'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inns.Album']", 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'high_season': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'inn_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_premium': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'machine_name': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'primary_key': 'True'}),
            'map_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'max_price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'default': '25.0', 'max_length': '50', 'max_digits': '3', 'blank': 'True', 'null': 'True'}),
            'min_price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'default': '20.0', 'max_length': '50', 'max_digits': '3', 'blank': 'True', 'null': 'True'}),
            'movil': ('django.db.models.fields.CharField', [], {'default': "u'(+53) '", 'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u'Hostal - '", 'max_length': '30'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "u'(01-41) '", 'max_length': '30'}),
            'rooms': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        'inns.reservationkey': {
            'Meta': {'object_name': 'ReservationKey'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inns.BookRoom']"}),
            'c_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'client_key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'i_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inn_key': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['inns']