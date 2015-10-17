# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Label.tracking_number'
        db.delete_column(u'oneminutelabel_label', 'tracking_number')

        # Adding field 'Label.amount'
        db.add_column(u'oneminutelabel_label', 'amount',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=8, decimal_places=4),
                      keep_default=False)

        # Adding field 'Label.label_url'
        db.add_column(u'oneminutelabel_label', 'label_url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=2048, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Label.tracking_number'
        db.add_column(u'oneminutelabel_label', 'tracking_number',
                      self.gf('django.db.models.fields.CharField')(default='[NONE]', max_length=100, db_index=True),
                      keep_default=False)

        # Deleting field 'Label.amount'
        db.delete_column(u'oneminutelabel_label', 'amount')

        # Deleting field 'Label.label_url'
        db.delete_column(u'oneminutelabel_label', 'label_url')


    models = {
        u'oneminutelabel.label': {
            'Meta': {'object_name': 'Label'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '4'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label_url': ('django.db.models.fields.URLField', [], {'max_length': '2048', 'blank': 'True'}),
            'rate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'label'", 'to': u"orm['oneminutelabel.Rate']"}),
            'shippo_object_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
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