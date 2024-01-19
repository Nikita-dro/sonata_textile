from unittest import mock

from django.test import TestCase
from django.urls import reverse
from rest_framework.status import (HTTP_200_OK, HTTP_401_UNAUTHORIZED,
                                   HTTP_403_FORBIDDEN)
from rest_framework.test import APIClient

from accounts.utils.samples import sample_customer
from products.utils.samples import sample_product


class TestAPI(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.product = sample_product(article=3254, name="TestName", size="30x30", price=500.00)

        self.user = sample_customer(email="api@test.com")
        self.user.set_password("1q2w3e4r")
        self.user.save()

        self.superuser = sample_customer(email="api_superuser@test.com", is_staff=True, is_superuser=True)
        self.superuser.set_password("1q2w3e")
        self.superuser.save()

    def tearDown(self):
        self.client.logout()

    def test_customer_list(self):
        self.client.force_authenticate(user=self.superuser)

        result = self.client.get(reverse("api:customers_all"))
        self.assertEqual(result.status_code, HTTP_200_OK)
        self.assertEqual(
            result.data,
            [
                {
                    "id": 1,
                    "first_name": "TestFirstName",
                    "last_name": "TestLastName",
                    "email": "api@test.com",
                    "phone_number": None,
                    "is_staff": False,
                },
                {
                    "id": 2,
                    "first_name": "TestFirstName",
                    "last_name": "TestLastName",
                    "email": "api_superuser@test.com",
                    "phone_number": None,
                    "is_staff": True,
                },
            ],
        )

    def test_customer_list_forbidden(self):
        self.client.force_authenticate(user=self.user)

        result = self.client.get(reverse("api:customers_all"))
        self.assertEqual(result.status_code, HTTP_403_FORBIDDEN)

    def test_products_details(self):
        self.client.force_authenticate(user=self.user)

        result = self.client.get(
            reverse(
                "api:product_one",
                kwargs={"pk": self.product.pk},
            )
        )

        self.assertEqual(result.status_code, HTTP_200_OK)
        self.assertEqual(
            result.data,
            {
                "id": mock.ANY,
                "article": 3254,
                "name": "TestName",
                "avatar": None,
                "category": {"id": mock.ANY, "name": "TestCategory"},
                "brand": {"id": mock.ANY, "name": "TestBrand"},
                "price": "UAH500.00",
                "size": "30x30",
                "material": mock.ANY,
                "producing_country": {"id": mock.ANY, "name": "TestProducingCountry"},
                "availability": True,
                "hit_sale": False,
                "description": "TestDescription",
            },
        )

    def test_product_details_no_access(self):
        result = self.client.get(reverse("api:product_one", kwargs={"pk": self.product.pk}))
        self.assertEqual(result.status_code, HTTP_401_UNAUTHORIZED)

    def test_product_list_access(self):
        result = self.client.get(reverse("api:products_all"))
        self.assertEqual(result.status_code, HTTP_200_OK)
