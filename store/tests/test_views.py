from django.test import TestCase, Client
from django.urls import reverse
from django.core.cache import cache
from category.models import Category
from .models import Product

class ProductAddViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Electronics', slug='electronics')
        self.add_product_url = reverse('add_product')

    def test_add_product_success(self):
        # Prepare POST data for creating a product
        data = {
            'name': 'Test Product',
            'slug': 'test-product',
            'price': '99.99',
            'description': 'This is a test product',
            'stock': 10,
            'is_available': True,
            'category': self.category.id,  # ForeignKey needs ID
        }

        # Ensure the cache key is set (simulate cache usage)
        cache.set('products_cache_key', 'dummy_cache', 300)

        response = self.client.post(self.add_product_url, data)

        # After success, the response should redirect to dashboard
        self.assertEqual(response.status_code, 302)  # Redirect status

        # Product should be created in DB
        product_exists = Product.objects.filter(slug='test-product').exists()
        self.assertTrue(product_exists)

        # Cache key should be deleted (no longer set)
        self.assertIsNone(cache.get('products_cache_key'))

    def test_add_product_invalid_data(self):
        # Missing required fields, e.g., price
        data = {
            'name': 'Invalid Product',
            'slug': 'invalid-product',
            # 'price' missing
            'description': 'Missing price',
            'stock': 5,
            'is_available': True,
            'category': self.category.id,
        }

        response = self.client.post(self.add_product_url, data)

        # Form is invalid, page re-rendered with errors (status 200)
        self.assertEqual(response.status_code, 200)

        # Product should NOT be created
        self.assertFalse(Product.objects.filter(slug='invalid-product').exists())
