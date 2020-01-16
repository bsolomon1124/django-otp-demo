# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login

from project import settings


@login_required
def hello(request):
    return HttpResponse("Hello")


def handle_login(request):
    if request.method == "POST":
        token = request.POST["token"]
        user = authenticate(request=request, token=token)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(request.POST.get("next") or settings.LOGIN_REDIRECT_URL)
        return render(request, "app/login.html", {"error": True, "next": request.POST["next"]})
    elif request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        return render(request, "app/login.html", {"next": request.GET.get("next", "")})
