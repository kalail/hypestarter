# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Artist.song_1'
        db.add_column('artists_artist', 'song_1',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Artist.song_2'
        db.add_column('artists_artist', 'song_2',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Artist.song_1'
        db.delete_column('artists_artist', 'song_1')

        # Deleting field 'Artist.song_2'
        db.delete_column('artists_artist', 'song_2')


    models = {
        'artists.artist': {
            'Meta': {'object_name': 'Artist'},
            'bandcamp_page': ('django.db.models.fields.URLField', [], {'max_length': '256', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'facebook_page': ('django.db.models.fields.URLField', [], {'max_length': '256', 'blank': 'True'}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artists.Genre']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_alt': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'itunes_link': ('django.db.models.fields.URLField', [], {'max_length': '256', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'song_1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'song_2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'soundcloud_page': ('django.db.models.fields.URLField', [], {'max_length': '256', 'blank': 'True'}),
            'twitter_handle': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'youtube_page': ('django.db.models.fields.URLField', [], {'max_length': '256', 'blank': 'True'})
        },
        'artists.genre': {
            'Meta': {'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['artists']