from django.db import models
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=50, null=True, blank=True, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='photos/category', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['-created_at']
        
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
    def __str__(self):
        return (self.category_name)
