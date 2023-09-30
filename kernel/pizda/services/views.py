from django.http import HttpResponse

def api(request, service):
    respone = "You requested " + service
    return HttpResponse(respone)
