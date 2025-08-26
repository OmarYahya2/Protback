import ssl

from django.core.mail.backends.smtp import EmailBackend as DjangoEmailBackend


class InsecureEmailBackend(DjangoEmailBackend):
    """SMTP backend that disables SSL certificate verification.

    NOTE: For local development/testing ONLY. Do not use in production.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Force an unverified SSL context for local dev
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        self.ssl_context = context


