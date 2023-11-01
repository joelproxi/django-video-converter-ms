from rest_framework.decorators import APIView
from rest_framework.response import Response

from config.services import AuthService


class LoginAPIView(APIView):
    def post(self, request):
        data = request.data

        resp = AuthService(request).authenticate(data, 'login/')
        if resp.status_code == 200:
            return Response(resp.json(), status=resp.status_code)
        print(resp)
        return Response(data=resp.json(), status=resp.status_code)


class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data

        resp = AuthService(request).authenticate(data, 'register/')
        if resp.status_code == 200:
            return Response(resp.json(), status=resp.status_code)
        print(resp)
        return Response(data=resp.json(), status=resp.status_code)
