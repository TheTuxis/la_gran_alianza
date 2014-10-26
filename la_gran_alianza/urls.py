from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'la_gran_alianza.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^api/', include('apps.api.urls')),
    url(
        r'^$',
        RedirectView.as_view(url='/main/', permanent=False),
        name='index'
    ),
    url(
        r'^main/',
        include(
            'apps.core.urls',
            namespace='core',
            app_name='core'
        )
    ),
    # url(
    #     r'^api/',
    #     include('apps.api.urls')
    # ),
)
