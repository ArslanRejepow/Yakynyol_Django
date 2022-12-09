from django.urls import path
from .views import add_service, add_to_favourites, add_to_favourites_service, delete_service, home, add_product, profile, profile_service, services, update_product_view, update_product, delete_product

urlpatterns = [
    path('', home, name='shopping'),
    path('add_product', add_product, name='add_product'),
    path('add_service', add_service, name='add_service'),
    path('profile', profile, name='profile_market'),
    path('profile/service', profile_service, name='profile_service'),
    path('update_product/<str:pk>', update_product_view,
         name='update_product_view'),
    path('update_pro', update_product, name='update_product'),
    path("delete_product/<str:pk>", delete_product, name="delete_product"),
    path("delete_service/<str:pk>", delete_service, name="delete_service"),
    path("add_to_favourites_product", add_to_favourites,
         name='add_to_favourites_product'),
    path("add_to_favourites_service", add_to_favourites_service,
         name='add_to_favourites_service'),
    path('services', services, name='services')
]
