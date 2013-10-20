# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Preparazione.Categoria'
        db.delete_column(u'ricette_preparazione', 'Categoria_id')

        # Adding field 'Preparazione.categoria'
        db.add_column(u'ricette_preparazione', 'categoria',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='preparazione', to=orm['ricette.CategoriaPreparazione']),
                      keep_default=False)

        # Adding field 'Preparazione.ingredients'
        db.add_column(u'ricette_preparazione', 'ingredients',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)

        # Adding field 'Preparazione.preparation'
        db.add_column(u'ricette_preparazione', 'preparation',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Preparazione.Categoria'
        db.add_column(u'ricette_preparazione', 'Categoria',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='preparazione', to=orm['ricette.CategoriaPreparazione']),
                      keep_default=False)

        # Deleting field 'Preparazione.categoria'
        db.delete_column(u'ricette_preparazione', 'categoria_id')

        # Deleting field 'Preparazione.ingredients'
        db.delete_column(u'ricette_preparazione', 'ingredients')

        # Deleting field 'Preparazione.preparation'
        db.delete_column(u'ricette_preparazione', 'preparation')


    models = {
        'ricette.categoria': {
            'Meta': {'ordering': "['nome']", 'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '50'}),
            'portata': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'ricette.categoriapreparazione': {
            'Meta': {'ordering': "['nome']", 'object_name': 'CategoriaPreparazione'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'ricette.lista': {
            'Meta': {'ordering': "['nome']", 'object_name': 'Lista'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'ricette.preparazione': {
            'Meta': {'ordering': "['nome']", 'object_name': 'Preparazione'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'preparazione'", 'to': "orm['ricette.CategoriaPreparazione']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.TextField', [], {'default': 'None'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'preparation': ('django.db.models.fields.TextField', [], {})
        },
        'ricette.ricetta': {
            'Meta': {'ordering': "['nome']", 'object_name': 'Ricetta'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ricette'", 'to': "orm['ricette.Categoria']"}),
            'costo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'difficulty': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ingredients': ('django.db.models.fields.TextField', [], {}),
            'lista': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ricette'", 'null': 'True', 'to': "orm['ricette.Lista']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'preparation': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'spotlight_recipe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time': ('django.db.models.fields.IntegerField', [], {}),
            'week_recipe': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['ricette']