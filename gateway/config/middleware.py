
from config.services import AuthService


def auth_middleware(get_response):

    def middleware(request):
        try:
            user = AuthService(request).get_user_info('user/').json()
        except:
            user = None
        print(user)
        request.user_svc = user

        response = get_response(request)
        return response
    return middleware