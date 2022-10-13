from django.contrib import admin
from app_car_api.models import Colors, Brands, CarModels, Orders


@admin.register(Colors)
class ColorsAdmin(admin.ModelAdmin):
    """
    Регистрация и отображения модели Colors в админке
    """
    list_display = ['color_name']
    list_display_links = ['color_name']


@admin.register(Brands)
class BrandAdmin(admin.ModelAdmin):
    """
    Регистрация и отображения модели Colors в админке
    """
    list_display = ['brand_name']


@admin.register(CarModels)
class CarModelsAdmin(admin.ModelAdmin):
    """
    Регистрация и отображения модели CarModels в админке
    """
    list_display = ['models_name', 'brand']
    list_display_links = ['models_name']
    list_filter = ['brand']


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    """
    Регистрация и отображение модели Orders в админке
    """
    list_display = ['color', 'model', 'quantity', 'orders_date']
    list_filter = ['color', 'model']
