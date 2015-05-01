# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dmeventsapp', '0002_auto_20150428_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweetId', models.CharField(max_length=20)),
                ('tweetText', models.CharField(max_length=140)),
                ('scoring', models.IntegerField()),
                ('judgeComments', models.TextField()),
                ('participant', models.ForeignKey(related_name='answers', to='dmeventsapp.Participant')),
                ('question', models.ForeignKey(related_name='answers', to='dmeventsapp.Question')),
            ],
        ),
        migrations.RemoveField(
            model_name='response',
            name='participant',
        ),
        migrations.RemoveField(
            model_name='response',
            name='question',
        ),
        migrations.DeleteModel(
            name='Response',
        ),
    ]
