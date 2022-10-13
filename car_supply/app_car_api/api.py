from app_car_api.models import Orders, Brands, CarModels, Colors
from app_car_api.serializers import OrdersGetSerializer, OrdersPostSerializer, BrandsSerializer, \
    ColorsSerializer, CarModelsGetSerializer, CarModelsPostSerializer
from app_car_api.api_pagination import OrdersPagination
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class OrdersApiViewSet(ModelViewSet):
    """
    API заказов автомобилей
    """

    queryset = Orders.objects.all()
    pagination_class = OrdersPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['model__brand']
    ordering_fields = ['quantity']

    serializer_classes = {'create': OrdersPostSerializer,
                          'update': OrdersPostSerializer}
    default_serializer_class = OrdersGetSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class ColorsApiViewSet(ModelViewSet):
    """
    API справочника цветов автомобилей
    """

    queryset = Colors.objects.all()
    serializer_class = ColorsSerializer


class CarModelsViewSet(ModelViewSet):
    """
    API справочника моделей автомобилей
    """

    queryset = CarModels.objects.select_related('brand').all()

    serializer_classes = {'create': CarModelsPostSerializer,
                          'update': CarModelsPostSerializer}
    default_serializer_class = CarModelsGetSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class BrandsApiViewSet(ModelViewSet):
    """
    API справочника брендов автомобилей
    """

    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer
