# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('hashtag', models.CharField(max_length=15)),
                ('startDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('endDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('instructions', models.TextField()),
                ('prizes', models.TextField()),
                ('link', models.CharField(max_length=200)),
                ('imagePath', models.CharField(max_length=200)),
                ('visibility', models.CharField(default=b'PUB', max_length=3, choices=[(b'PRI', b'Private'), (b'PUB', b'Public')])),
                ('noSocialSharing', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('twitterHandle', models.CharField(max_length=20)),
                ('event', models.ForeignKey(related_name='participants', to='dmeventsapp.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qTitle', models.CharField(max_length=200)),
                ('qExplanation', models.TextField()),
                ('qType', models.CharField(default=b'P', max_length=2, choices=[(b'V', b'Video'), (b'P', b'Photo')])),
                ('qPoints', models.IntegerField()),
                ('event', models.ForeignKey(related_name='questions', to='dmeventsapp.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweetId', models.CharField(max_length=20)),
                ('tweetText', models.CharField(max_length=140)),
                ('scoring', models.IntegerField()),
                ('judgeComments', models.TextField()),
                ('participant', models.ForeignKey(related_name='responses', to='dmeventsapp.Participant')),
                ('question', models.ForeignKey(related_name='responses', to='dmeventsapp.Question')),
            ],
        ),
    ]
