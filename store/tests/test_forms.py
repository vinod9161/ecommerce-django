from django.test import TestCase
from .forms import ProductForm
from category.models import Category

class ProductFormTest(TestCase):
    def test_valid_form(self):
        category = Category.objects.create(name="Cat1", slug="cat1")
        data = {'name': 'Test Product', 'slug': 'test-product', 'price': '9.99', 'description': 'desc', 'stock': 10, 'category': category.id}
        form = ProductForm(data=data)
        self.assertTrue(form.is_valid())
