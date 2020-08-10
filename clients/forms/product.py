from django import forms

from products.models import Brand, Category, Product


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('name', 'short_description', 'description',
                  'logo', 'feature_image', 'status')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'parent_id', 'description',
                  'logo', 'feature_image', 'status')

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        if kwargs['instance']:
            sub_category = list(kwargs['instance'].parent_category.values_list('id', flat=True))
            sub_category.append(kwargs['instance'].id)
            self.fields['parent_id'].queryset = Category.objects.exclude(id__in=sub_category)

        self.fields['parent_id'].label = "Parent Category"
        self.fields['parent_id'].widget.attrs['class'] = 'form-control selectpicker'
        self.fields['parent_id'].widget.attrs['data-live-search'] = 'true'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category_id', 'brand_id', 'price', 'unit', 'sku', 'purchase_limit', 'purchase_limit_quantity', 'discounted',
                  'discounted_price', 'on_offer', 'featured', 'badge', 'vat', 'vat_rate', 'short_description', 'image', 'description', 'status')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category_id'].label = "Category Name"
        self.fields['category_id'].widget.attrs['class'] = 'form-control selectpicker'
        self.fields['category_id'].widget.attrs['data-live-search'] = 'true'
        self.fields['brand_id'].label = "Brand Name"
        self.fields['brand_id'].widget.attrs['class'] = 'form-control selectpicker'
        self.fields['brand_id'].widget.attrs['data-live-search'] = 'true'
        self.fields['purchase_limit'].widget.attrs['class'] = 'form-control selectpicker'
        self.fields['discounted'].widget.attrs['class'] = 'form-control selectpicker'
        self.fields['on_offer'].widget.attrs['class'] = 'form-control selectpicker'
        self.fields['featured'].widget.attrs['class'] = 'form-control selectpicker'
        self.fields['badge'].widget.attrs['class'] = 'form-control selectpicker'
        self.fields['vat'].widget.attrs['class'] = 'form-control selectpicker'
        self.fields['purchase_limit_quantity'].label = "Purchase Limit Quantity"
