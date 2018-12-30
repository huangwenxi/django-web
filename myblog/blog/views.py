# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def article_page(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})

def edit_page(request, article_id=None):
    if article_id == '0':
        return render(request, 'blog/edit_page.html')
    article = Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})

def edit_action(request, article_id=None):
    title = request.POST.get('title')
    content = request.POST.get('content')

    if article_id == "0":
        Article.objects.create(title=title, content=content)
    else:
        article = Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def delete_action(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.delete()
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})








