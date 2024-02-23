"""
Tests for health check API.
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class HealthCheckAPITest(APITestCase):
    def test_health_check(self):
        url = reverse('health-check')  # Replace 'health-check' with the actual URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
