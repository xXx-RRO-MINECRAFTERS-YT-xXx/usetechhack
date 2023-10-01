from django.http import HttpResponse
from django.template import loader

from random import choice

def api(request, service):
    has_access = choice([True, False])
    if has_access:
        respone = "You requested " + service + " and request was given, cuz u have access"
        return HttpResponse(respone)
    else:
        respone = "You haven't permission to view this page!"
        return HttpResponse(respone, status=403)
