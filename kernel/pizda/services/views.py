from django.http import HttpResponse
from django.template import loader

from random import choice

import jwt
from django.http import JsonResponse
from config.keycloak_settings import get_public_key


def verify_token(request):
    token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[-1]
    public_key = get_public_key()

    try:
        decoded_token = jwt.decode(token, public_key, algorithms=['RS256'])
        decoded_token
        return JsonResponse({'message': 'Токен действителен', 'decoded_token': decoded_token})
    except jwt.exceptions.InvalidTokenError:
        return JsonResponse({'message': 'Недействительный токен'}, status=401)

def api(request, service):
    has_access = choice([True, False])
    tok = verify_token(request)
    if tok != JsonResponse({'message': 'Недействительный токен'}, status=401):
        if has_access:
            respone = "You requested " + service + " and request was given, cuz u have access"
            return HttpResponse(respone)
        else:
            respone = "You haven't permission to view this page!"
            return HttpResponse(respone, status=403)
    else:
        return tok
