from django.contrib import admin
from .models import Product

admin.site.site_header = 'CLAVIS PRODUCT API'
admin.site.site_title = 'CLAVIS PRODUCT API'

admin.site.register(Product)
