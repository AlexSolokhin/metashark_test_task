from django.urls import path
from app_car_api.api import OrdersApiViewSet, CarModelsViewSet, ColorsApiViewSet,  BrandsApiViewSet

urlpatterns = [
    path('orders/', OrdersApiViewSet.as_view({'get': 'list',
                                              'post': 'create'}), name='orders_list_api'),
    path('orders/<int:pk>', OrdersApiViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update',
                                                      'delete': 'destroy'}), name='orders_detail_api'),
    path('car_models/', CarModelsViewSet.as_view({'get': 'list',
                                                  'post': 'create'}), name='car_models_list_api'),
    path('car_models/<int:pk>', CarModelsViewSet.as_view({'get': 'retrieve',
                                                          'put': 'update',
                                                          'delete': 'destroy'}), name='car_models_detail_api'),
    path('colors/', ColorsApiViewSet.as_view({'get': 'list',
                                              'post': 'create'}), name='colors_list_api'),
    path('colors/<int:pk>', ColorsApiViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update',
                                                      'delete': 'destroy'}), name='colors_detail_api'),
    path('brands/', BrandsApiViewSet.as_view({'get': 'list',
                                              'post': 'create'}), name='brands_list_api'),
    path('brands/<int:pk>', BrandsApiViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update',
                                                      'delete': 'destroy'}), name='brands_detail_api'),
]
