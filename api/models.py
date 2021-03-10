from django.db import models

class Product(models.Model):
  title = models.CharField(max_length=255, blank=True, null=True)
  sku = models.CharField(max_length=255, blank=True, null=True)
  price = models.CharField(max_length=255, blank=True, null=True)

  def __srt__(self):
    return self.title

