from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import City, Product, Photo

class ProductAPITests(APITestCase):

    def setUp(self):
        self.city1 = City.objects.create(name="New York")
        self.city2 = City.objects.create(name="Los Angeles")

        self.product1 = Product.objects.create(name="Product 1")
        self.product2 = Product.objects.create(name="Product 2")

        self.photo1 = Photo.objects.create(product=self.product1, city=self.city1, image_url="http://example.com/photo1.jpg")
        self.photo2 = Photo.objects.create(product=self.product1, city=None, image_url="http://example.com/photo2.jpg")
        self.photo3 = Photo.objects.create(product=self.product2, city=self.city2, image_url="http://example.com/photo3.jpg")

    def test_product_with_city_specific_photos(self):
        url = reverse('product-detail')
        response = self.client.get(url, {'city_id': self.city1.id, 'product_name': 'Product 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['photos']), 1)
        self.assertEqual(response.data['photos'][0]['image_url'], 'http://example.com/photo1.jpg')

    def test_product_with_general_photos(self):
        url = reverse('product-detail')
        response = self.client.get(url, {'city_id': self.city2.id, 'product_name': 'Product 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['photos']), 1)
        self.assertEqual(response.data['photos'][0]['image_url'], 'http://example.com/photo2.jpg')

    def test_product_with_no_matching_city(self):
        url = reverse('product-detail')  
        response = self.client.get(url, {'city_id': 999, 'product_name': 'Product 1'}) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['photos']), 1)
        self.assertEqual(response.data['photos'][0]['image_url'], 'http://example.com/photo2.jpg')

    def test_missing_product_name(self):
        url = reverse('product-detail')
        response = self.client.get(url, {'city_id': self.city1.id})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('product_name query parameter is required.', response.data['detail'])

    def test_product_with_no_photos(self):
        product_no_photos = Product.objects.create(name="Product 3")
        url = reverse('product-detail')
        response = self.client.get(url, {'city_id': self.city1.id, 'product_name': 'Product 3'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['photos']), 0)

