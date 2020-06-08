from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_price = models.IntegerField()
    product_description = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    text = models.TextField()