# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rate'
        db.create_table(u'oneminutelabel_rate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=4)),
            ('shippo_object_id', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
        ))
        db.send_create_signal(u'oneminutelabel', ['Rate'])

        # Adding model 'Label'
        db.create_table(u'oneminutelabel_label', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('rate', self.gf('django.db.models.fields.related.ForeignKey')(related_name='label', to=orm['oneminutelabel.Rate'])),
            ('shippo_object_id', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('tracking_number', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
        ))
        db.send_create_signal(u'oneminutelabel', ['Label'])


    def backwards(self, orm):
        # Deleting model 'Rate'
        db.delete_table(u'oneminutelabel_rate')

        # Deleting model 'Label'
        db.delete_table(u'oneminutelabel_label')


    models = {
        u'oneminutelabel.label': {
            'Meta': {'object_name': 'Label'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'label'", 'to': u"orm['oneminutelabel.Rate']"}),
            'shippo_object_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'tracking_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'oneminutelabel.rate': {
            'Meta': {'object_name': 'Rate'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '4'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shippo_object_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        }
    }

    complete_apps = ['oneminutelabel']