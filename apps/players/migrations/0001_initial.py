# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='History_Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pagina', models.ForeignKey(blank=True, to='books.Pagina', null=True)),
                ('pregunta', models.ForeignKey(blank=True, to='books.Pregunta', null=True)),
                ('respuesta', models.ForeignKey(blank=True, to='books.Respuesta', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('puntuacion_total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('puntuacion', models.DecimalField(max_digits=10, decimal_places=2)),
                ('finish', models.BooleanField(default=False)),
                ('last_activity', models.DateTimeField(default=datetime.datetime.now)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('libro', models.ForeignKey(blank=True, to='books.Libro', null=True)),
                ('profile', models.ForeignKey(blank=True, to='players.Profile', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='history_session',
            name='session',
            field=models.ForeignKey(blank=True, to='players.Session', null=True),
            preserve_default=True,
        ),
    ]
