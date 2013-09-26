# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Categoria.slug'
        db.add_column(u'ricette_categoria', 'slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Categoria.slug'
        db.delete_column(u'ricette_categoria', 'slug')


    models = {
        'ricette.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'portata': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ricette.Portata']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True'})
        },
        'ricette.portata': {
            'Meta': {'object_name': 'Portata'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'ricette.ricetta': {
            'Meta': {'object_name': 'Ricetta'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ricette.Categoria']"}),
            'costo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'difficulty': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.TextField', [], {}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'preparation': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True'}),
            'spotlight_recipe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time': ('django.db.models.fields.IntegerField', [], {}),
            'week_recipe': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['ricette']