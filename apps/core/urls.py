from django.conf.urls import patterns, url
from django.views.generic import TemplateView


class SimpleStaticView(TemplateView):
    def get_template_names(self):
        return [self.kwargs.get('template_name') + ".html"]

    def get(self, request, *args, **kwargs):
        from django.contrib.auth import authenticate, login
        if request.user.is_anonymous():
            # Auto-login the User for Demonstration Purposes
            user = authenticate()
            login(request, user)
        return super(SimpleStaticView, self).get(request, *args, **kwargs)


urlpatterns = patterns(
    '',
    url(
        r'^$',
        'apps.core.views.main',
        name='main'
    ),
    url(
        r'^(?P<template_name>\w+)$', SimpleStaticView.as_view(),
        name='example'
    ),
)
