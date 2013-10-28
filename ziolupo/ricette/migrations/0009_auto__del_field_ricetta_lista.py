# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Ricetta.lista'
        db.delete_column(u'ricette_ricetta', 'lista_id')

        # Adding M2M table for field lista on 'Ricetta'
        m2m_table_name = db.shorten_name(u'ricette_ricetta_lista')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ricetta', models.ForeignKey(orm['ricette.ricetta'], null=False)),
            ('lista', models.ForeignKey(orm['ricette.lista'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ricetta_id', 'lista_id'])


    def backwards(self, orm):
        # Adding field 'Ricetta.lista'
        db.add_column(u'ricette_ricetta', 'lista',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='ricette', null=True, to=orm['ricette.Lista'], blank=True),
                      keep_default=False)

        # Removing M2M table for field lista on 'Ricetta'
        db.delete_table(db.shorten_name(u'ricette_ricetta_lista'))


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
            'ingredients': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
            'lista': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'ricette'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['ricette.Lista']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'preparation': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'spotlight_recipe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time': ('django.db.models.fields.IntegerField', [], {}),
            'week_recipe': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['ricette']