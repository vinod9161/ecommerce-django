from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(name="Test", slug="test", price=10, description="desc", stock=5, category_id=1)
        self.assertEqual(product.name, "Test")
