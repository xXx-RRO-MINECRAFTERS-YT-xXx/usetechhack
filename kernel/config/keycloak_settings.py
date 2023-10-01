import requests
import json
from jwt.algorithms import RSAAlgorithm

KEYCLOAK_URL = 'https://your-keycloak-url/auth/realms/your-realm'
KEY_ID = 'your-key-id'


def get_public_key():
    response = requests.get(f'{KEYCLOAK_URL}/protocol/openid-connect/certs')
    keys = response.json()['keys']
    public_key = None

    for key in keys:
        if key['kid'] == KEY_ID:
            public_key = RSAAlgorithm.from_jwk(json.dumps(key))
            break

    if not public_key:
        raise Exception('Открытый ключ не найден')

    return public_key
