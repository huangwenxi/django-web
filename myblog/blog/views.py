# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article


def index(request):
    return render(request, 'blog/index.html', {'hello':'hello blog'})
