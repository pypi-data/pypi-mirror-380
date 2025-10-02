"""Function tests for the `/research/grants/<pk>/` endpoint."""

from datetime import date

from rest_framework.test import APITestCase

from apps.research_products.factories import GrantFactory
from .common import ResearchDetailEndpointPermissionsTestMixin


class EndpointPermissions(ResearchDetailEndpointPermissionsTestMixin, APITestCase):
    """Test endpoint user permissions.

    See the `ResearchDetailEndpointPermissionsTests` class docstring for details on the
    tested endpoint permissions.
    """

    factory = GrantFactory
    endpoint_pattern = '/research/grants/{pk}/'

    def build_valid_record_data(self) -> dict:
        """Return a dictionary containing valid Grant data."""

        return {
            'title': "Grant (Team 2)",
            'agency': "Agency Name",
            'amount': 1000,
            'start_date': date(2000, 1, 1),
            'end_date': date(2000, 1, 31),
            'grant_number': 'abc-123',
            'team': self.team.id
        }
