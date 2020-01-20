# https://docs.djangoproject.com/en/3.0/topics/http/middleware/
# Note that this varies from 'old style' middleware as shown at,
# for example,
# https://github.com/django/django/blob/master/django/middleware/security.py


def simple_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Tk
        response.setdefault("Tk", "N")
        return response
    return middleware
