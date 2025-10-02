"""Unit tests for the `LogRequestMiddleware` class."""

import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.test import override_settings, TestCase
from django.test.client import RequestFactory

from apps.logging.middleware import LogRequestMiddleware
from apps.logging.models import RequestLog
from apps.users.factories import UserFactory


class CidLogging(TestCase):
    """Test the extraction and logging of CID values from request headers."""

    def setUp(self) -> None:
        """Instantiate testing fixtures."""

        self.middleware = LogRequestMiddleware(lambda x: HttpResponse())

    @override_settings(AUDITLOG_CID_HEADER='X-CUSTOM-CID')
    def test_cid_header_logged(self) -> None:
        """Verify the CID value is correctly extracted and saved."""

        cid_value = str(uuid.uuid4())
        request = RequestFactory().get('/example/')
        request.META['HTTP_X_CUSTOM_CID'] = cid_value

        request.user = AnonymousUser()

        self.middleware(request)
        log = RequestLog.objects.first()
        self.assertEqual(cid_value, log.cid)

    def test_missing_cid_header(self) -> None:
        """Verify a valid CID value is automatically generated when the CID header is not present."""

        request = RequestFactory().get('/example/')
        request.user = AnonymousUser()
        self.middleware(request)

        log = RequestLog.objects.first()
        self.assertTrue(uuid.UUID(log.cid))


class ClientIPLogging(TestCase):
    """Test the extraction and logging of client IP values from request headers."""

    def setUp(self) -> None:
        """Instantiate testing fixtures."""

        self.middleware = LogRequestMiddleware(lambda x: HttpResponse())

    def test_logs_ip_from_x_forwarded_for(self) -> None:
        """Verify the client IP is logged from the `X-Forwarded-For` header."""

        request = RequestFactory().get('/test-ip/')
        request.META['HTTP_X_FORWARDED_FOR'] = '192.168.1.1, 10.0.0.1'
        request.META['REMOTE_ADDR'] = '192.168.2.2'
        request.user = AnonymousUser()

        self.middleware(request)
        log = RequestLog.objects.first()
        self.assertEqual('192.168.1.1', log.remote_address)

    def test_logs_ip_from_remote_addr(self) -> None:
        """Verify the client IP is logged from `REMOTE_ADDR` when `X-Forwarded-For` is missing."""

        request = RequestFactory().get('/test-ip/')
        request.META['REMOTE_ADDR'] = '192.168.1.1'
        request.user = AnonymousUser()

        self.middleware(request)
        log = RequestLog.objects.first()
        self.assertEqual('192.168.1.1', log.remote_address)

    def test_logs_none_if_no_ip_headers(self) -> None:
        """Verify `None` is logged when no IP headers are present."""

        request = RequestFactory().get('/test-ip/')
        request.user = AnonymousUser()
        request.META.pop('REMOTE_ADDR', None)  # Explicitly remove default IP

        self.middleware(request)
        log = RequestLog.objects.first()
        self.assertIsNone(log.remote_address)


class LoggingToDatabase(TestCase):
    """Test the logging of requests to the database."""

    def test_authenticated_user(self) -> None:
        """Verify requests are logged for authenticated users."""

        request = RequestFactory().get('/hello/')
        request.user = UserFactory()

        middleware = LogRequestMiddleware(lambda x: HttpResponse())
        middleware(request)

        self.assertEqual(1, RequestLog.objects.count())
        self.assertEqual(RequestLog.objects.first().user, request.user)

    def test_anonymous_user(self) -> None:
        """Verify requests are logged for anonymous users."""

        request = RequestFactory().get('/hello/')
        request.user = AnonymousUser()

        middleware = LogRequestMiddleware(lambda x: HttpResponse())
        middleware(request)

        self.assertEqual(1, RequestLog.objects.count())
        self.assertIsNone(RequestLog.objects.first().user)
