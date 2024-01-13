# Generated by Django 4.2.3 on 2024-01-10 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('product_details', models.TextField(blank=True, max_length=500)),
                ('product_image', models.ImageField(upload_to='images/products')),
                ('product_stock', models.IntegerField()),
                ('product_availability', models.BooleanField(default=True)),
                ('product_create_time', models.DateTimeField(auto_now_add=True)),
                ('product_modified_time', models.DateTimeField(auto_now=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.categoriesmodel')),
            ],
        ),
    ]
