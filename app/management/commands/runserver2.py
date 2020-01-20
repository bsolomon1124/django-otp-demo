# import os

from django.core.management.base import BaseCommand, CommandError
from django.core.wsgi import get_wsgi_application

import app.wsgiserver

# TODO: chrome://flags/#allow-insecure-localhost
# openssl req -newkey rsa:8192 -new -nodes -x509 -days 365 -keyout key.pem -out cert.pem


class Command(BaseCommand):
    help = 'Starts a production Web server via WSGIServer.'

    def add_arguments(self, parser):
        parser.add_argument("--host", default="127.0.0.1")
        parser.add_argument("--port", type=int, default=8080)
        parser.add_argument("--numthreads", type=int, default=10)
        parser.add_argument("--certfile")
        parser.add_argument("--keyfile")

    def handle(self, *args, **options):
        # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
        try:
            server = app.wsgiserver.WSGIServer(
                get_wsgi_application(),
                host=options["host"],
                port=options["port"],
                numthreads=options["numthreads"],
                certfile=options["certfile"],
                keyfile=options["keyfile"],
            )
        except Exception as e:
            raise
            # raise CommandError(str(e))
        if options["keyfile"] and options["certfile"]:
            protocol = "https"
        else:
            protocol = "http"
        self.stdout.write(
            self.style.SUCCESS(
                'Listening at %s://%s:%d/' % (protocol, options['host'], options['port'])
            )
        )
        server.start()
