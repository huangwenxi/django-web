# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(max_length=32, default='Content')

    def __str__(self):
        return self.title


class Animal(models.Model):
    name = models.CharField(max_length=32, default='...')

    def __str__(self):
        return self.name
