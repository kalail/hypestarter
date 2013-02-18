# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ('artists', '0002_auto__add_artist__add_genre'),
    )

    def forwards(self, orm):
        # Adding model 'Featured'
        db.create_table('landing_featured', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('landing', ['Featured'])

        # Adding M2M table for field artists on 'Featured'
        db.create_table('landing_featured_artists', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('featured', models.ForeignKey(orm['landing.featured'], null=False)),
            ('artist', models.ForeignKey(orm['artists.artist'], null=False))
        ))
        db.create_unique('landing_featured_artists', ['featured_id', 'artist_id'])


    def backwards(self, orm):
        # Deleting model 'Featured'
        db.delete_table('landing_featured')

        # Removing M2M table for field artists on 'Featured'
        db.delete_table('landing_featured_artists')


    models = {
        'artists.artist': {
            'Meta': {'object_name': 'Artist'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artists.Genre']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'artists.genre': {
            'Meta': {'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'landing.featured': {
            'Meta': {'object_name': 'Featured'},
            'artists': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['artists.Artist']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['landing']