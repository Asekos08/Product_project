from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Product, City
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import ProductSerializer, PhotoSerializer

class ProductDetailView(APIView):

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'City-ID', 
                openapi.IN_HEADER, 
                description="ID города для фильтрации фотографий", 
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                'product_name', 
                openapi.IN_QUERY, 
                description="Название продукта для поиска", 
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={200: ProductSerializer}
    )
    def get(self, request, *args, **kwargs):
        city_id = request.headers.get('city_id')
        product_name = request.query_params.get('product_name')

        if not product_name:
            return Response({"detail": "product_name query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(name=product_name)
        except Product.DoesNotExist:
            raise Http404("Product not found.")

        if city_id:
            try:
                city = City.objects.get(pk=city_id)
            except City.DoesNotExist:
                photos = product.photos.filter(city__isnull=True)
            else:
                photos = product.photos.filter(city=city)
                if not photos.exists():
                    photos = product.photos.filter(city__isnull=True)
        else:
            photos = product.photos.filter(city__isnull=True)

        photo_serializer = PhotoSerializer(photos, many=True)
        product_data = ProductSerializer(product).data
        product_data['photos'] = photo_serializer.data 

        return Response(product_data, status=status.HTTP_200_OK)