# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=150)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=150)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('contenido', models.TextField(max_length=3000)),
                ('numero', models.IntegerField(null=True, blank=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('capitulo', models.ForeignKey(blank=True, to='books.Capitulo', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=150)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('puntuacion', models.DecimalField(max_digits=10, decimal_places=2)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('pregunta', models.ForeignKey(blank=True, to='books.Pregunta', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pagina',
            name='pregunta',
            field=models.ForeignKey(blank=True, to='books.Pregunta', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='capitulo',
            name='libro',
            field=models.ForeignKey(blank=True, to='books.Libro', null=True),
            preserve_default=True,
        ),
    ]
