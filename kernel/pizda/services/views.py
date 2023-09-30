from django.http import HttpResponse
from django.template import loader

def api(request, service):
    respone = "You requested " + service
    return HttpResponse(respone)

def password_reset(request):
    return HttpResponse("BAZA")
