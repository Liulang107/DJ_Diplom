from .views import order_created
from django.urls import path

app_name = 'orders'
urlpatterns = [
    path('', order_created, name='order_created'),
]
