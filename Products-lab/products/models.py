from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    tags = models.TextField(null=True, blank=True)
    thumbnail = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    cover = models.ImageField(upload_to="products/%Y/%m/%d/" ,null=True ,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
