from django.core.management.base import BaseCommand
from products.models import City, Product, Photo
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Seed the database with cities, products, and photos'

    def handle(self, *args, **kwargs):
        Photo.objects.all().delete()
        Product.objects.all().delete()
        City.objects.all().delete()

        city1 = City.objects.create(name="New York")
        city2 = City.objects.create(name="Los Angeles")
        city3 = City.objects.create(name="Chicago")

        product1 = Product.objects.create(name="Product A")
        product2 = Product.objects.create(name="Product B")
        product3 = Product.objects.create(name="Product C")

        photo1 = Photo.objects.create(product=product1, city=None, image_url="media/photos/product_a_general.jpg")
        photo2 = Photo.objects.create(product=product1, city=city1, image_url="media/photos/product_a_ny.jpg")
        photo3 = Photo.objects.create(product=product2, city=None, image_url="media/photos/product_b_general.jpg")
        photo4 = Photo.objects.create(product=product2, city=city2, image_url="media/photos/product_b_la.jpg")
        photo5 = Photo.objects.create(product=product3, city=None, image_url="media/photos/product_c_general.jpg")
        photo6 = Photo.objects.create(product=product3, city=city3, image_url="media/photos/product_c_chicago.jpg")

        self.stdout.write(self.style.SUCCESS("Database seeded successfully"))
