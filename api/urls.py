from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('products/', views.products_view, name='products_view'),
    path('update/', views.update_prices, name='update_prices')
]
