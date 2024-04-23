from django.db import models
from categories.models import categories
from django.db.models.fields.files import ImageField


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=False)
    categories = models.ForeignKey('categories.Categories', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.title