# encoding: utf-8
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'Visit'
        db.create_table('visits_visit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('visitor_hash', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=40, null=True, blank=True)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(db_index=True, max_length=15, null=True, blank=True)),
            ('last_visit', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('visits', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('object_app', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('object_model', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('object_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('blocked', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('visits', ['Visit'])

    def backwards(self, orm):

        # Deleting model 'Visit'
        db.delete_table('visits_visit')

    models = {
        'visits.visit': {
            'Meta': {'ordering': "('uri', 'object_model', 'object_id')", 'object_name': 'Visit'},
            'blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'db_index': 'True', 'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'last_visit': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'object_app': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_model': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visitor_hash': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'visits': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['visits']
