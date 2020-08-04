from django.db import models
from products.models import Product

# Create your models here.


class Stock(models.Model):
    product_id = models.ForeignKey(
        Product, null=True, blank=True, related_name='stock_product_name', on_delete=models.SET_NULL)
    quantity = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Report(models.Model):
    product_id = models.ForeignKey(
        Product, null=True, blank=True, related_name='report_product_name', on_delete=models.SET_NULL)
    opening_stock = models.IntegerField(null=True, blank=True)
    purchase_quantity = models.IntegerField(null=True, blank=True)
    purchase_return_quantity = models.IntegerField(null=True, blank=True)
    sale_quantity = models.IntegerField(null=True, blank=True)
    sale_return_quantity = models.IntegerField(null=True, blank=True)
    report_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class History(models.Model):
    product_id = models.ForeignKey(
        Product, null=True, blank=True, related_name='history_product_name', on_delete=models.SET_NULL)
    previous_stock = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    current_stock = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
