import pytest
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer

from apps.space.views import SpacesViewSet


class TestViews:
    @pytest.mark.django_db
    def test_view_check_pytest(self):
        path = reverse('space-list')
        request = RequestFactory().get(path)

        response = SpacesViewSet.as_view({'get': 'list'})(request)
        assert response.status_code == 200
