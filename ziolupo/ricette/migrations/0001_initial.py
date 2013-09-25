# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Portata'
        db.create_table(u'ricette_portata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('ricette', ['Portata'])

        # Adding model 'Categoria'
        db.create_table(u'ricette_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('portata', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ricette.Portata'])),
        ))
        db.send_create_signal('ricette', ['Categoria'])

        # Adding model 'Ricetta'
        db.create_table(u'ricette_ricetta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ricette.Categoria'])),
            ('ingredients', self.gf('django.db.models.fields.TextField')()),
            ('difficulty', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('preparation', self.gf('django.db.models.fields.TextField')()),
            ('costo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('time', self.gf('django.db.models.fields.IntegerField')()),
            ('week_recipe', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('spotlight_recipe', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('ricette', ['Ricetta'])


    def backwards(self, orm):
        # Deleting model 'Portata'
        db.delete_table(u'ricette_portata')

        # Deleting model 'Categoria'
        db.delete_table(u'ricette_categoria')

        # Deleting model 'Ricetta'
        db.delete_table(u'ricette_ricetta')


    models = {
        'ricette.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'portata': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ricette.Portata']"})
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
            'spotlight_recipe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time': ('django.db.models.fields.IntegerField', [], {}),
            'week_recipe': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['ricette']