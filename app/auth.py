from django.contrib.auth.models import User

from project import settings

# https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#writing-an-authentication-backend


class OTPBackend(object):
    def authenticate(self, request, token=None):
        if token == settings.MAGIC_TOKEN:
            user, _ = User.objects.get_or_create(username="foobar")
            return user
        return None

    def get_user(self, user_id):
        return User.objects.get_or_create(username="foobar")[0]
