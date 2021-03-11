from django.db import models


class Product(models.Model):
    RETAILER_CHOICES = (
        ("ARTICLE", "Article"),
        ("BOUCLAIR", "Bouclair"),
        ("CRATE_&_BARREL", "Crate & Barrel"),
        ("ELTE", "ELTE"),
        ("EQ3", "EQ3"),
        ("WAYFAIR", "Wayfair"),
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    retailer = models.CharField(max_length=255, choices=RETAILER_CHOICES)
    price = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
