from django.test import TestCase
from django.urls import reverse

class AnsatteTests(TestCase):
    def test_index_laster(self):
        response = self.client.get(reverse("ansatte:index"))
        self.assertEqual(response.status_code, 200)
