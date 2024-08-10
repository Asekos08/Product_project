from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)

class Photo(models.Model):
    product = models.ForeignKey(Product, related_name='photos', on_delete=models.CASCADE)
    image_url = models.URLField()
    city = models.ForeignKey(City, related_name='photos', on_delete=models.CASCADE, null=True, blank=True)