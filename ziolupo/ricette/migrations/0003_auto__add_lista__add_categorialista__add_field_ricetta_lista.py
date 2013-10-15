# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lista'
        db.create_table(u'ricette_lista', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(related_name='liste', to=orm['ricette.CategoriaLista'])),
        ))
        db.send_create_signal(u'ricette', ['Lista'])

        # Adding model 'CategoriaLista'
        db.create_table(u'ricette_categorialista', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'ricette', ['CategoriaLista'])

        # Adding field 'Ricetta.lista'
        db.add_column(u'ricette_ricetta', 'lista',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='ricette', null=True, to=orm['ricette.Lista']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Lista'
        db.delete_table(u'ricette_lista')

        # Deleting model 'CategoriaLista'
        db.delete_table(u'ricette_categorialista')

        # Deleting field 'Ricetta.lista'
        db.delete_column(u'ricette_ricetta', 'lista_id')


    models = {
        'ricette.categoria': {
            'Meta': {'ordering': "['nome']", 'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "' '", 'max_length': '50'}),
            'portata': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'ricette.categorialista': {
            'Meta': {'object_name': 'CategoriaLista'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ricette.lista': {
            'Meta': {'object_name': 'Lista'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'liste'", 'to': u"orm['ricette.CategoriaLista']"}),
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
            'lista': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ricette'", 'null': 'True', 'to': u"orm['ricette.Lista']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'preparation': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'spotlight_recipe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time': ('django.db.models.fields.IntegerField', [], {}),
            'week_recipe': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['ricette']