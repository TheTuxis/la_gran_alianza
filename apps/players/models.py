# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from apps.books.models import Pagina, Libro, Pregunta, Respuesta
import datetime


# comentario


class Profile(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    puntuacion_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return "%s" % (self.user,)


class Session(models.Model):
    profile = models.ForeignKey(Profile, blank=True, null=True)
    libro = models.ForeignKey(Libro, blank=True, null=True)
    puntuacion = models.DecimalField(max_digits=10, decimal_places=2)
    finish = models.BooleanField(default=False)
    last_activity = models.DateTimeField(default=datetime.datetime.now)
    date_created = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return "%s, %s" % (self.profile, self.libro)


class History_Session(models.Model):
    session = models.ForeignKey(Session, blank=True, null=True)
    pagina = models.ForeignKey(Pagina, blank=True, null=True)
    pregunta = models.ForeignKey(Pregunta, blank=True, null=True)
    respuesta = models.ForeignKey(Respuesta, blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.session,)
