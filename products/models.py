from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=240)
    slug = models.CharField(max_length=240)
    short_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='brands/logo/', blank=True, null=True)
    feature_image = models.ImageField(
        upload_to='brands/features/', blank=True, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=240)
    slug = models.CharField(max_length=240)
    parent_id = models.ForeignKey(
        "self", null=True, related_name='parent_category', on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to='category/icon/', blank=True, null=True)
    feature_image = models.ImageField(
        upload_to='category/features/', blank=True, null=True)
    status = models.BooleanField(default=True)
    show_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    YES_NO_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No')
    )

    name = models.CharField(max_length=240)
    slug = models.CharField(max_length=240)
    category_id = models.ForeignKey(
        Category, null=True, related_name='category', on_delete=models.SET_NULL)
    brand_id = models.ForeignKey(
        Brand, null=True, related_name='brand', on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50, null=True, blank=True)
    sku = models.CharField(max_length=100, null=True, blank=True)
    purchase_limit = models.CharField(max_length=5, choices=YES_NO_CHOICES,default='No')
    purchase_limit_quantity = models.IntegerField(blank=True, null=True)
    discounted = models.CharField(max_length=5, choices=YES_NO_CHOICES,default='No')
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    on_offer = models.CharField(max_length=5, choices=YES_NO_CHOICES,default='No')
    featured = models.CharField(max_length=5, choices=YES_NO_CHOICES,default='No')
    badge = models.CharField(max_length=10, choices=(('sale','Sale'),('hot','Hot'),('limited','Limited')), null=True, blank=True)
    vat = models.CharField(max_length=5, choices=YES_NO_CHOICES,default='No')
    vat_rate =  models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    short_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

