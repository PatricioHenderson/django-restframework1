from django.urls import path
from e_commerce.api.e_commerce_api import *
from e_commerce.api.marvel_api_views import *


urlpatterns = [
    path('stock/' , stock),
    path('price/' , price) ,
    path('cart/' , cart) ,
    path('get_comics/' , get_comics) ,
    path('purchased_item/', purchased_item ),
]