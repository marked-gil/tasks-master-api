from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import REST_AUTH


@api_view()
def root_route(request):
    return Response({
        'message': 'You have reached the API for Tasks Master'
    })


@api_view(['POST'])
def logout_route(request):
    """
    Fix to dj-rest-auth logout view
    [As suggested from CI drf_api walkthrough project]
    """
    response = Response()
    response.set_cookie(
        key=REST_AUTH["JWT_AUTH_COOKIE"],
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=REST_AUTH["JWT_AUTH_SAMESITE"],
        secure=REST_AUTH["JWT_AUTH_SECURE"],
    )
    response.set_cookie(
        key=REST_AUTH["JWT_AUTH_REFRESH_COOKIE"],
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=REST_AUTH["JWT_AUTH_SAMESITE"],
        secure=REST_AUTH["JWT_AUTH_SECURE"],
    )
    return response
