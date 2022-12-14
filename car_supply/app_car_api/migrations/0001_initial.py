# Generated by Django 4.1.2 on 2022-10-12 16:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=30, verbose_name='brand')),
            ],
        ),
        migrations.CreateModel(
            name='CarModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('models_name', models.CharField(max_length=50, verbose_name='model')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='app_car_api.brands', verbose_name='brand')),
            ],
        ),
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=30, verbose_name='color_name')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message="Quantity can't be lower than 1")], verbose_name='quantity')),
                ('orders_date', models.DateField(default=django.utils.timezone.now, verbose_name='date')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app_car_api.colors', verbose_name='color')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app_car_api.carmodels', verbose_name='model')),
            ],
        ),
    ]
