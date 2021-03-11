from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.CharField(max_length=255, blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
