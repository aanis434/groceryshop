# Generated by Django 3.1 on 2020-08-07 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200807_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discounted',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='on_offer',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_limit',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='vat',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=5),
        ),
    ]
