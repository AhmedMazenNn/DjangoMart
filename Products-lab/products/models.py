from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

available_categories = [("Beauty", "beauty"),
                        ("technology","technology"),
                        ("health","health"),
                        ("groceries","groceries")
                        ]

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    tags = models.TextField(null=True)
    thumbnail = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")