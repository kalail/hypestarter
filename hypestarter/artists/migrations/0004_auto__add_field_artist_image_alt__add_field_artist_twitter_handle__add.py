# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Artist.image_alt'
        db.add_column('artists_artist', 'image_alt',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Artist.twitter_handle'
        db.add_column('artists_artist', 'twitter_handle',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True),
                      keep_default=False)

        # Adding field 'Artist.itunes_link'
        db.add_column('artists_artist', 'itunes_link',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=256, blank=True),
                      keep_default=False)

        # Adding field 'Artist.soundcloud_page'
        db.add_column('artists_artist', 'soundcloud_page',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=256, blank=True),
                      keep_default=False)

        # Adding field 'Artist.youtube_page'
        db.add_column('artists_artist', 'youtube_page',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=256, blank=True),
                      keep_default=False)

        # Adding field 'Artist.bandcamp_page'
        db.add_column('artists_artist', 'bandcamp_page',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=256, blank=True),
                      keep_default=False)

        # Adding field 'Artist.facebook_page'
        db.add_column('artists_artist', 'facebook_page',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=256, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Artist.image_alt'
        db.delete_column('artists_artist', 'image_alt')

        # Deleting field 'Artist.twitter_handle'
        db.delete_column('artists_artist', 'twitter_handle')

        # Deleting field 'Artist.itunes_link'
        db.delete_column('artists_artist', 'itunes_link')

        # Deleting field 'Artist.soundcloud_page'
        db.delete_column('artists_artist', 'soundcloud_page')

        # Deleting field 'Artist.youtube_page'
        db.delete_column('artists_artist', 'youtube_page')

        # Deleting field 'Artist.bandcamp_page'
        db.delete_column('artists_artist', 'bandcamp_page')

        # Deleting field 'Artist.facebook_page'
        db.delete_column('artists_artist', 'facebook_page')


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