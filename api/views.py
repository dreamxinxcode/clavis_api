from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/products/',
    }
    return Response(api_urls)


@api_view(['GET'])
def api_overview(request):
