# -*- coding: utf-8 -*-

from django.db import models

class HttpRequest(models.Model):
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.method} {self.path}"
