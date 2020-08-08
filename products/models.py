import os

from django.db import models

# Create your models here.
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.urls import reverse


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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('clients:brand')


class Category(models.Model):
    name = models.CharField(max_length=240)
    slug = models.CharField(max_length=240)
    parent_id = models.ForeignKey(
        "self", null=True, blank=True, related_name='parent_category', on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='category/logo/', blank=True, null=True)
    feature_image = models.ImageField(
        upload_to='category/features/', blank=True, null=True)
    status = models.BooleanField(default=True)
    show_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('clients:category')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


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
    purchase_limit = models.CharField(
        max_length=5, choices=YES_NO_CHOICES, default='no')
    purchase_limit_quantity = models.IntegerField(blank=True, null=True)
    discounted = models.CharField(
        max_length=5, choices=YES_NO_CHOICES, default='no')
    discounted_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    on_offer = models.CharField(
        max_length=5, choices=YES_NO_CHOICES, default='no')
    featured = models.CharField(
        max_length=5, choices=YES_NO_CHOICES, default='no')
    badge = models.CharField(max_length=10, choices=(('sale', 'Sale'), ('hot', 'Hot'), ('limited', 'Limited')),
                             null=True, blank=True)
    vat = models.CharField(max_length=5, choices=YES_NO_CHOICES, default='no')
    vat_rate = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    short_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


@receiver(models.signals.post_delete, sender=Brand)
@receiver(models.signals.post_delete, sender=Category)
@receiver(models.signals.post_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if sender != 'Product':
        if instance.logo:
            if os.path.isfile(instance.logo.path):
                os.remove(instance.logo.path)

        if instance.feature_image:
            if os.path.isfile(instance.feature_image.path):
                os.remove(instance.feature_image.path)
    else:
        if instance.image:
            if os.path.isfile(instance.image.path):
                os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=Brand)
@receiver(models.signals.pre_save, sender=Category)
@receiver(models.signals.pre_save, sender=Product)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    if sender != 'Product':
        try:
            old_logo = sender.objects.get(pk=instance.pk).logo
        except sender.DoesNotExist:
            return False

        new_logo = instance.logo
        if old_logo and not old_logo == new_logo:
            if os.path.isfile(old_logo.path):
                os.remove(old_logo.path)

        try:
            old_feature_image = sender.objects.get(pk=instance.pk).feature_image
        except sender.DoesNotExist:
            return False

        new_feature_image = instance.feature_image
        if old_feature_image and not old_feature_image == new_feature_image:
            if os.path.isfile(old_feature_image.path):
                os.remove(old_feature_image.path)
    else:
        try:
            old_image = sender.objects.get(pk=instance.pk).image
        except sender.DoesNotExist:
            return False

        new_image = instance.image
        if old_image and not old_image == new_image:
            if os.path.isfile(old_image.path):
                os.remove(old_image.path)
