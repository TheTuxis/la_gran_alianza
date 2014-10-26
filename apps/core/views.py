# -*- coding: utf-8 -*-
from django.db.models import Q
from datetime import date, timedelta
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext


@login_required
def main(request, id_causa=0, id_typo_tarea=0, ejecutar_tarea=0):
    return render_to_response(
        'core/main.html',
        RequestContext(
            request,
            {}
        )
    )
