"""Function tests for the `/allocations/comments/` endpoint."""

from rest_framework import status
from rest_framework.test import APITestCase

from apps.allocations.factories import AllocationRequestFactory, CommentFactory
from apps.users.factories import MembershipFactory, UserFactory
from apps.users.models import Membership
from tests.utils import CustomAsserts, TeamListFilteringTestMixin

ENDPOINT = '/allocations/comments/'


class EndpointPermissions(APITestCase, CustomAsserts):
    """Test endpoint user permissions.

    Endpoint permissions are tested against the following matrix of HTTP responses.
    Permissions depend on the user's role within the team owning the accessed record.

    | Authentication | GET | HEAD | OPTIONS | POST | PUT | PATCH | DELETE | TRACE |
    |----------------|-----|------|---------|------|-----|-------|--------|-------|
    | Anonymous User | 401 | 401  | 401     | 401  | 401 | 401   | 401    | 401   |
    | Non-Member     | 200 | 200  | 200     | 403  | 405 | 405   | 405    | 405   |
    | Team Member    | 200 | 200  | 200     | 201  | 405 | 405   | 405    | 405   |
    | Team Admin     | 200 | 200  | 200     | 201  | 405 | 405   | 405    | 405   |
    | Team Owner     | 200 | 200  | 200     | 201  | 405 | 405   | 405    | 405   |
    | Staff User     | 200 | 200  | 200     | 201  | 405 | 405   | 405    | 405   |
    """

    endpoint = ENDPOINT

    def setUp(self) -> None:
        """Create test fixtures using mock data."""

        self.request = AllocationRequestFactory()

        self.team = self.request.team
        self.team_member = MembershipFactory(team=self.team, role=Membership.Role.MEMBER).user
        self.team_admin = MembershipFactory(team=self.team, role=Membership.Role.ADMIN).user
        self.team_owner = MembershipFactory(team=self.team, role=Membership.Role.OWNER).user

        self.non_member = UserFactory()
        self.staff_user = UserFactory(is_staff=True)

        self.valid_record_data = {'content': 'foo', 'request': self.request.pk}

    def test_anonymous_user_permissions(self) -> None:
        """Verify unauthenticated users cannot access resources."""

        self.assert_http_responses(
            self.endpoint,
            get=status.HTTP_401_UNAUTHORIZED,
            head=status.HTTP_401_UNAUTHORIZED,
            options=status.HTTP_401_UNAUTHORIZED,
            post=status.HTTP_401_UNAUTHORIZED,
            put=status.HTTP_401_UNAUTHORIZED,
            patch=status.HTTP_401_UNAUTHORIZED,
            delete=status.HTTP_401_UNAUTHORIZED,
            trace=status.HTTP_401_UNAUTHORIZED
        )

    def test_non_team_member_permissions(self) -> None:
        """Verify users have read access but cannot create records for teams where they are not members."""

        self.client.force_authenticate(user=self.non_member)
        self.assert_http_responses(
            self.endpoint,
            get=status.HTTP_200_OK,
            head=status.HTTP_200_OK,
            options=status.HTTP_200_OK,
            post=status.HTTP_403_FORBIDDEN,
            put=status.HTTP_405_METHOD_NOT_ALLOWED,
            patch=status.HTTP_405_METHOD_NOT_ALLOWED,
            delete=status.HTTP_405_METHOD_NOT_ALLOWED,
            trace=status.HTTP_405_METHOD_NOT_ALLOWED,
            post_body=self.valid_record_data
        )

    def test_team_member_permissions(self) -> None:
        """Verify regular team members have read-only access."""

        self.client.force_authenticate(user=self.team_member)
        self.assert_http_responses(
            self.endpoint,
            get=status.HTTP_200_OK,
            head=status.HTTP_200_OK,
            options=status.HTTP_200_OK,
            post=status.HTTP_201_CREATED,
            put=status.HTTP_405_METHOD_NOT_ALLOWED,
            patch=status.HTTP_405_METHOD_NOT_ALLOWED,
            delete=status.HTTP_405_METHOD_NOT_ALLOWED,
            trace=status.HTTP_405_METHOD_NOT_ALLOWED,
            post_body=self.valid_record_data
        )

    def test_team_admin_permissions(self) -> None:
        """Verify team admins have read and write access."""

        self.client.force_authenticate(user=self.team_admin)
        self.assert_http_responses(
            self.endpoint,
            get=status.HTTP_200_OK,
            head=status.HTTP_200_OK,
            options=status.HTTP_200_OK,
            post=status.HTTP_201_CREATED,
            put=status.HTTP_405_METHOD_NOT_ALLOWED,
            patch=status.HTTP_405_METHOD_NOT_ALLOWED,
            delete=status.HTTP_405_METHOD_NOT_ALLOWED,
            trace=status.HTTP_405_METHOD_NOT_ALLOWED,
            post_body=self.valid_record_data
        )

    def test_team_owner_permissions(self) -> None:
        """Verify team owners have read and write access."""

        self.client.force_authenticate(user=self.team_owner)
        self.assert_http_responses(
            self.endpoint,
            get=status.HTTP_200_OK,
            head=status.HTTP_200_OK,
            options=status.HTTP_200_OK,
            post=status.HTTP_201_CREATED,
            put=status.HTTP_405_METHOD_NOT_ALLOWED,
            patch=status.HTTP_405_METHOD_NOT_ALLOWED,
            delete=status.HTTP_405_METHOD_NOT_ALLOWED,
            trace=status.HTTP_405_METHOD_NOT_ALLOWED,
            post_body=self.valid_record_data
        )

    def test_staff_user_permissions(self) -> None:
        """Verify staff users have read and write permissions."""

        self.client.force_authenticate(user=self.staff_user)
        self.assert_http_responses(
            self.endpoint,
            get=status.HTTP_200_OK,
            head=status.HTTP_200_OK,
            options=status.HTTP_200_OK,
            post=status.HTTP_201_CREATED,
            put=status.HTTP_405_METHOD_NOT_ALLOWED,
            patch=status.HTTP_405_METHOD_NOT_ALLOWED,
            delete=status.HTTP_405_METHOD_NOT_ALLOWED,
            trace=status.HTTP_405_METHOD_NOT_ALLOWED,
            post_body=self.valid_record_data
        )


class PrivateRecordFiltering(APITestCase):
    """Test the filtering of returned records based on their `private` status."""

    endpoint = ENDPOINT

    def setUp(self) -> None:
        """Create test fixtures using mock data."""

        self.request = AllocationRequestFactory()
        self.team = self.request.team
        self.team_member = MembershipFactory(team=self.team, role=Membership.Role.MEMBER).user

        self.staff_user = UserFactory(is_staff=True)

        self.public_comment = CommentFactory(request=self.request, user=self.team_member, private=False)
        self.private_comment = CommentFactory(request=self.request, user=self.staff_user, private=True)

    def test_staff_includes_private_records(self) -> None:
        """Verify staff users are returned public and private records."""

        self.client.force_authenticate(user=self.staff_user)
        response = self.client.get(self.endpoint)
        returned_ids = [r['id'] for r in response.json()]

        expected_ids = [self.public_comment.id, self.private_comment.id]
        self.assertCountEqual(expected_ids, returned_ids)

    def test_nonstaff_excludes_private_records(self) -> None:
        """Verify non-staff users are only returned public records."""

        self.client.force_authenticate(user=self.team_member)
        response = self.client.get(self.endpoint)
        returned_ids = [r['id'] for r in response.json()]

        expected_ids = [self.public_comment.id, ]
        self.assertCountEqual(expected_ids, returned_ids)


class TeamRecordFiltering(TeamListFilteringTestMixin, APITestCase):
    """Test the filtering of returned records based on user team membership."""

    endpoint = ENDPOINT
    factory = CommentFactory
    team_field = 'request__team'
