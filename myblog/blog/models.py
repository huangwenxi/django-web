# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(max_length=32, default='Content')

    def __str__(self):
        return self.title
