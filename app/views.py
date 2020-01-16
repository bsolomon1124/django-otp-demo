# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def hello(request):
    print(request.user)
    print(request.session)
    return HttpResponse("Hello")
