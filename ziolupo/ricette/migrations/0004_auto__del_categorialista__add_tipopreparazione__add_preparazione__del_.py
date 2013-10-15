# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'CategoriaLista'
        db.delete_table(u'ricette_categorialista')

        # Adding model 'TipoPreparazione'
        db.create_table(u'ricette_tipopreparazione', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('ricette', ['TipoPreparazione'])

        # Adding model 'Preparazione'
        db.create_table(u'ricette_preparazione', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Tipo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='preparazione', to=orm['ricette.TipoPreparazione'])),
        ))
        db.send_create_signal('ricette', ['Preparazione'])

        # Deleting field 'Lista.categoria'
        db.delete_column(u'ricette_lista', 'categoria_id')


    def backwards(self, orm):
        # Adding model 'CategoriaLista'
        db.create_table(u'ricette_categorialista', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'ricette', ['CategoriaLista'])

        # Deleting model 'TipoPreparazione'
        db.delete_table(u'ricette_tipopreparazione')

        # Deleting model 'Preparazione'
        db.delete_table(u'ricette_preparazione')

        # Adding field 'Lista.categoria'
        db.add_column(u'ricette_lista', 'categoria',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='liste', to=orm['ricette.CategoriaLista']),
                      keep_default=False)


    models = {
        'ricette.categoria': {
            'Meta': {'ordering': "['nome']", 'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '50'}),
            'portata': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'ricette.lista': {
            'Meta': {'ordering': "['nome']", 'object_name': 'Lista'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'ricette.preparazione': {
            'Meta': {'ordering': "['nome']", 'object_name': 'Preparazione'},
            'Tipo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'preparazione'", 'to': "orm['ricette.TipoPreparazione']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        },
        'ricette.tipopreparazione': {
            'Meta': {'ordering': "['nome']", 'object_name': 'TipoPreparazione'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ricette']