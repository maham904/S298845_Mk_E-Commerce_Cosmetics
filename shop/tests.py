from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .models import Product
from django.urls import reverse
from decimal import Decimal  # ✅ needed for Decimal comparison

class ProductModelTest(TestCase):
    def setUp(self):
        Product.objects.create(
            name="Lipstick Red",
            description="Classic red lipstick",
            price=Decimal('9.99')  # ✅ use Decimal for DecimalField
        )

    def test_product_creation(self):
        product = Product.objects.get(name="Lipstick Red")
        self.assertEqual(product.name, "Lipstick Red")
        self.assertEqual(str(product), "Lipstick Red")  # __str__ check

    def test_product_price(self):
        product = Product.objects.get(name="Lipstick Red")
        self.assertEqual(product.price, Decimal('9.99'))  # ✅ compare Decimal with Decimal

    class ProductViewTest(TestCase):
        def setUp(self):
            image = SimpleUploadedFile(
                name="test_image.jpg",
                content=b"",  # empty content is fine for tests
                content_type="lipsticks/png"
            )
            Product.objects.create(
                name="Lipstick Pink",
                description="Soft pink shade",
                price=Decimal('12.50'),
                image=image  # ✅ add this
            )

    def test_homepage_loads(self):
        # ✅ Make sure the URL name matches your urls.py
        # If your urls.py has namespace 'shop', use reverse("shop:product_list")
        response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lipstick Pink")
