from django.db import models
from django.core.validators import MinValueValidator
from django.utils.timezone import now as current_time


class Colors(models.Model):
    """
    Модель для цветов.
    Содержит наименования цвета.
    """

    color_name = models.CharField(max_length=30, verbose_name='color_name')

    @property
    def total_auto(self):
        queryset = self.orders.all().aggregate(total_auto=models.Sum('quantity'))
        return queryset['total_auto']

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'
        ordering = ['color_name']

    def __str__(self):
        return self.color_name


class Brands(models.Model):
    """
    Модель для марок автомобилей.
    Содержит наименование марки.
    """

    brand_name = models.CharField(max_length=30, verbose_name='brand')

    @property
    def total_auto(self):
        queryset = self.models.all().aggregate(total_auto=models.Sum('orders__quantity'))
        return queryset['total_auto']

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
        ordering = ['brand_name']

    def __str__(self):
        return self.brand_name


class CarModels(models.Model):
    """
    Модель для моделей автомобилей.
    Содержит наименование модели и марку (ForeignKey)
    """

    models_name = models.CharField(max_length=50, verbose_name='model')
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, verbose_name='brand', related_name='models')

    class Meta:
        verbose_name = 'car model'
        verbose_name_plural = 'car models'
        ordering = ['models_name']

    def __str__(self):
        return f'{self.brand.brand_name} {self.models_name}'


class Orders(models.Model):
    """
    Модель для заказов автомобилей.
    """

    color = models.ForeignKey(Colors, on_delete=models.CASCADE, verbose_name='color', related_name='orders')
    model = models.ForeignKey(CarModels, on_delete=models.CASCADE, verbose_name='model', related_name='orders')
    quantity = models.IntegerField(verbose_name='quantity',
                                   validators=[MinValueValidator(1, message="Quantity can't be lower than 1")])
    orders_date = models.DateField(verbose_name='date', default=current_time().date)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        ordering = ['orders_date']

    def __str__(self):
        return f'{self.model.brand.brand_name} {self.model.models_name} {self.color.color_name} {self.quantity}'
