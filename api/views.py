from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from .utils import *
import time


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/products/',
    }
    return Response(api_urls)


@api_view(['GET'])
def products_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def update_prices(request):
    for product in Product.objects.all():
        url = product.url
        price = fetch_price(product)
        product.price = price
        product.save()
        time.sleep(.25)

    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
