from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator ,RegexValidator
from django.contrib.auth import get_user_model
User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message="Title must contain only letters and spaces."
            )
        ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message="Title must contain only letters and spaces."
            )
        ]
    )
    description = models.TextField()
    price = models.PositiveIntegerField(
        validators=[MaxValueValidator(10000)],
        help_text="Price should not exceed 10,000."
    )
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text="Rating must be between 0 and 5."
    )
    tags = models.TextField(null=True, blank=True)
    thumbnail = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    cover = models.ImageField(upload_to="products/%Y/%m/%d/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

