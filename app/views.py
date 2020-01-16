# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse


@login_required
def hello(request):
    print(request.user)
    print(request.session)
    return HttpResponse("Hello")
