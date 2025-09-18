from django.test import TestCase
from .models import Product
from django.urls import reverse

class ProductModelTest(TestCase):
    def setUp(self):
        Product.objects.create(
            name="Lipstick Red",
            description="Classic red lipstick",
            price=9.99
        )

    def test_product_creation(self):
        product = Product.objects.get(name="Lipstick Red")
        self.assertEqual(product.name, "Lipstick Red")
        self.assertEqual(str(product), "Lipstick Red")  # __str__ check

    def test_product_price(self):
        product = Product.objects.get(name="Lipstick Red")
        self.assertEqual(product.price, 9.99)

class ProductViewTest(TestCase):
    def setUp(self):
        Product.objects.create(
            name="Lipstick Pink",
            description="Soft pink shade",
            price=12.50
        )

    def test_homepage_loads(self):
        response = self.client.get(reverse("product_list"))  # adjust if your url name is different
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lipstick Pink")