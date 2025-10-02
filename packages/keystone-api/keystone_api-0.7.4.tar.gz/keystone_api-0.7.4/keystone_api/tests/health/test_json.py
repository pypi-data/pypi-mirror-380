"""Function tests for the `/health/json/` endpoint."""

from unittest.mock import Mock, patch

from rest_framework import status
from rest_framework.test import APITransactionTestCase

from apps.users.factories import UserFactory
from tests.utils import CustomAsserts


@patch('health_check.backends.BaseHealthCheckBackend.run_check', return_value=None)
class EndpointPermissions(APITransactionTestCase, CustomAsserts):
    """Test endpoint user permissions.

    Endpoint permissions are tested against the following matrix of HTTP responses.

    | User Status                | GET | HEAD | OPTIONS | POST | PUT | PATCH | DELETE | TRACE |
    |----------------------------|-----|------|---------|------|-----|-------|--------|-------|
    | Unauthenticated User       | 200 | 200  | 200     | 405  | 405 | 405   | 405    | 405   |
    | Authenticated User         | 200 | 200  | 200     | 405  | 405 | 405   | 405    | 405   |
    | Staff User                 | 200 | 200  | 200     | 405  | 405 | 405   | 405    | 405   |
    """

    endpoint = '/health/json/'

    def setUp(self) -> None:
        """Create test fixtures using mock data."""

        self.generic_user = UserFactory()
        self.staff_user = UserFactory(is_staff=True)

    def test_unauthenticated_user_permissions(self, _mock_run_check: Mock) -> None:
        """Verify unauthenticated users have read-only permissions."""

        self.assert_http_responses(
            self.endpoint,
            get=status.HTTP_200_OK,
            head=status.HTTP_200_OK,
            options=status.HTTP_200_OK,
            post=status.HTTP_405_METHOD_NOT_ALLOWED,
            put=status.HTTP_405_METHOD_NOT_ALLOWED,
            patch=status.HTTP_405_METHOD_NOT_ALLOWED,
            delete=status.HTTP_405_METHOD_NOT_ALLOWED,
            trace=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    def test_authenticated_user_permissions(self, _mock_run_check: Mock) -> None:
        """Verify authenticated users have read-only permissions."""

        self.client.force_authenticate(user=self.generic_user)
        self.assert_http_responses(
            self.endpoint,
            get=status.HTTP_200_OK,
            head=status.HTTP_200_OK,
            options=status.HTTP_200_OK,
            post=status.HTTP_405_METHOD_NOT_ALLOWED,
            put=status.HTTP_405_METHOD_NOT_ALLOWED,
            patch=status.HTTP_405_METHOD_NOT_ALLOWED,
            delete=status.HTTP_405_METHOD_NOT_ALLOWED,
            trace=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    def test_staff_user_permissions(self, _mock_run_check: Mock) -> None:
        """Verify staff users have read-only permissions."""

        self.client.force_authenticate(user=self.staff_user)
        self.assert_http_responses(
            self.endpoint,
            get=status.HTTP_200_OK,
            head=status.HTTP_200_OK,
            options=status.HTTP_200_OK,
            post=status.HTTP_405_METHOD_NOT_ALLOWED,
            put=status.HTTP_405_METHOD_NOT_ALLOWED,
            patch=status.HTTP_405_METHOD_NOT_ALLOWED,
            delete=status.HTTP_405_METHOD_NOT_ALLOWED,
            trace=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
