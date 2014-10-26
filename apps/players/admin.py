from django.contrib import admin
from apps.players.models import Profile, Session, History_Session


admin.site.register(Profile)
admin.site.register(Session)
admin.site.register(History_Session)
