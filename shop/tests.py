from django.test import TestCase
from django.urls import reverse
from shop.models import Product
from django.core.files.uploadedfile import SimpleUploadedFile
from decimal import Decimal

class ProductViewTest(TestCase):
    def setUp(self):
        # Create an in-memory fake image
        image_content = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xFF\xFF\xFF\x21\xF9\x04\x00\x00\x00\x00\x00\x2C\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4C\x01\x00\x3B'
        image = SimpleUploadedFile("lipstik.png", image_content, content_type="image/png")

        Product.objects.create(
            name="Lipstick Pink",
            description="Soft pink shade",
            price=Decimal('12.50'),
            image=image
        )

    def test_homepage_loads(self):
        response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lipstick Pink")
