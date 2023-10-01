import jwt
from datetime import datetime, timedelta
from django.conf import settings

def generate_jwt_token(user_id, access: str):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(minutes=5),
        # Добавьте любые дополнительные поля данных, которые вы хотите включить в токен
        'access': access,
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

def decode_jwt_token(token):
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        # Обработка исключения истекшего токена
        return None
    except jwt.InvalidTokenError:
        # Обработка исключения недействительного токена
        return None
