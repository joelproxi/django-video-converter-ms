from rest_framework.decorators import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status
from core.authentications import JWTAuthentication
from core.models import UserModel

from core.serializers import UserModelSerializer
from core.utils import populate_database_with_token


class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        print(data)
        if data['password'] != data['confirm_password']:
            raise AuthenticationFailed(detail='Your password do not match')
        serializer = UserModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # generate_token function here
        token = JWTAuthentication.generate_token(user.id)
        populate_database_with_token(user.id, token)
        return Response({"token": token, 'id': user.id},
                        status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    def post(self, request):
        data = request.data
        print(data)
        email, password = data['email'], data['password']
        if not email or not password:
            raise AuthenticationFailed(
                detail='Please enter your email or password')

        user = UserModel.objects.filter(email=email).first()
        if not user:
            raise AuthenticationFailed(
                detail='Acount with this email not found')

        if not user.check_password(password):
            raise AuthenticationFailed(
                detail='Your email and password dit Not match')

        # generate_token here
        token = JWTAuthentication.generate_token(user.pk)
        populate_database_with_token(user.id, token)
        return Response({"token": token, 'id': user.pk})
