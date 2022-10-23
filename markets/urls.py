from django.urls import path
from .views import home, add_product, profile, update_product_view, update_product, delete_product

urlpatterns = [
    path('', home, name='shopping'),
    path('add_product', add_product, name='add_product'),
    path('profile', profile, name='profile_market'),
    path('update_product/<str:pk>', update_product_view, name='update_product_view'),
    path('update_pro', update_product, name='update_product'),
    path("delete_product/<str:pk>", delete_product, name="delete_product"),
]