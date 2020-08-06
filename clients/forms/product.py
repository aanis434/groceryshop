from django import forms

from products.models import Brand


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('name', 'short_description', 'description', 'logo', 'feature_image', 'status')


