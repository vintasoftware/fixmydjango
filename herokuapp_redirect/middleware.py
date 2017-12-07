from django.conf import settings
from django.http import HttpResponseRedirect


def _get_redirect_response(request):
    new_location = '{protocol}://{host}{full_path}'.format(
        protocol=settings.PROTOCOL,
        host=settings.DOMAIN,
        full_path=request.get_full_path()
    )
    return HttpResponseRedirect(new_location)


class CustomDomainRedirectMiddleware:

    def __init__(self, get_response):
        # One-time configuration and initialization.
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        http_host = request.get_host()

        if getattr(settings, 'HEROKUAPP_REDIRECT_ACTIVE', False) and 'herokuapp' in http_host:
            return _get_redirect_response(request)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
