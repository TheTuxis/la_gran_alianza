# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime


# comentario


class Pregunta(models.Model):

    name = models.CharField(max_length=20)
    description = models.TextField(max_length=150)
    author = models.ForeignKey(User, blank=True, null=True)
    date_created = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return "%s" % (self.name,)


class Respuesta(models.Model):

    pregunta = models.ForeignKey(Pregunta, blank=True, null=True)
    name = models.CharField(max_length=20)
    puntuacion = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(User, blank=True, null=True)
    date_created = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return "%s" % (self.name,)


class Libro(models.Model):

    name = models.CharField(max_length=20)
    description = models.TextField(max_length=150)
    author = models.ForeignKey(User, blank=True, null=True)
    date_created = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return "%s" % (self.name,)


class Capitulo(models.Model):

    libro = models.ForeignKey(Libro, blank=True, null=True)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=150)
    author = models.ForeignKey(User, blank=True, null=True)
    date_created = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return "%s" % (self.name,)


class Pagina(models.Model):

    capitulo = models.ForeignKey(Capitulo, blank=True, null=True)
    name = models.CharField(max_length=20)
    contenido = models.TextField(max_length=3000)
    pregunta = models.ForeignKey(Pregunta, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True)
    date_created = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return "%s" % (self.name,)
