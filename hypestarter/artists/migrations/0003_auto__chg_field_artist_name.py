# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Artist.name'
        db.alter_column('artists_artist', 'name', self.gf('django.db.models.fields.CharField')(max_length=256))

    def backwards(self, orm):

        # Changing field 'Artist.name'
        db.alter_column('artists_artist', 'name', self.gf('django.db.models.fields.CharField')(max_length=128))

    models = {
        'artists.artist': {
            'Meta': {'object_name': 'Artist'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artists.Genre']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'artists.genre': {
            'Meta': {'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['artists']