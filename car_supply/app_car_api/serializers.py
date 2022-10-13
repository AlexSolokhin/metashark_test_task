from rest_framework import serializers
from app_car_api.models import Orders, Colors, CarModels, Brands


class OrdersGetSerializer(serializers.ModelSerializer):
    """
    Класс serializer для заказов, используется для метода get
    """

    color = serializers.StringRelatedField()
    model = serializers.StringRelatedField()
    brand = serializers.CharField(source='model.brand', read_only=True)

    class Meta:
        model = Orders
        fields = ['orders_date', 'color', 'brand', 'model', 'quantity']


class OrdersPostSerializer(serializers.ModelSerializer):
    """
    Класс serializer для заказов, используется для методов post/put
    """

    class Meta:
        model = Orders
        fields = ['orders_date', 'color', 'model', 'quantity']


class ColorsSerializer(serializers.ModelSerializer):
    """
    Класс serializer для справочника цветов
    """

    class Meta:
        model = Colors
        fields = ['color_name', 'total_auto']


class CarModelsGetSerializer(serializers.ModelSerializer):
    """
    Класс serializer для справочника моделей автомобилей, используется для метода get
    """

    brand = serializers.StringRelatedField()

    class Meta:
        model = CarModels
        fields = ['models_name', 'brand']


class CarModelsPostSerializer(serializers.ModelSerializer):
    """
    Класс serializer для справочника моделей автомобилей, используется для методов post/put
    """

    class Meta:
        model = CarModels
        fields = ['models_name', 'brand']


class BrandsSerializer(serializers.ModelSerializer):
    """
    Класс serializer для справочника моделей автомобилей
    """

    class Meta:
        model = Brands
        fields = ['brand_name', 'total_auto']
