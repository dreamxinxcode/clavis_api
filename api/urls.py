from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview),
    path('products/', views.products_view),
]
