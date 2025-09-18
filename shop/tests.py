import os
from django.test import TestCase
from django.urls import reverse
from decimal import Decimal
from .models import Product
from django.core.files import File

class ProductViewTest(TestCase):
    def setUp(self):
        # Path to your actual image
        image_path = os.path.join(os.path.dirname(__file__), '..', 'media', 'lipsticks', 'lipstik.png')
        with open(image_path, 'rb') as f:
            product_image = File(f)
            Product.objects.create(
                name="Lipstick Pink",
                description="Soft pink shade",
                price=Decimal('12.50'),
                image=product_image
            )

    def test_homepage_loads(self):
        response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lipstick Pink")
