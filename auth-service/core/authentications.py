from datetime import datetime, timedelta, timezone
import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework import HTTP_HEADER_ENCODING
from rest_framework import exceptions

from config import settings
from core.models import TokenModel, UserModel


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        jwt_token = self.get_headers(request)
        if jwt_token is None:
            return None

        jwt_token = self.split_token(jwt_token)
        try:
            payload = jwt.decode(jwt=jwt_token,
                                 key=settings.SECRET_KEY,
                                 algorithms='HS256')
        except jwt.exceptions.InvalidSignatureError:
            raise exceptions.AuthenticationFailed(detail='Invalid signature')
        except Exception():
            raise exceptions.ParseError()

        user_id = payload.get('id')
        if user_id is None:
            raise exceptions.AuthenticationFailed('User not found')

        user = UserModel.objects.filter(id=user_id).first()
        if not TokenModel.objects.filter(
                user_id=user.id,
                token=jwt_token,
                expired_at__gt=datetime.now(tz=timezone.utc)).exists():
            raise BaseAuthentication('Unauthenticated')
        return user, payload

    @staticmethod
    def get_headers(request):
        auth = request.META.get('HTTP_AUTHORIZATION')
        return auth

    @staticmethod
    def split_token(token: str):
        return token.split(' ')[1]

    @staticmethod
    def generate_token(user_id):
        payload = {
            'id': user_id,
            'exp': datetime.utcnow() + timedelta(minutes=10),
            'iat': datetime.utcnow()
        }
        token = jwt.encode(payload=payload,
                           key=settings.SECRET_KEY,
                           algorithm='HS256')
        return token
