from .views import CartView, CheckoutView
from django.urls import path

app_name = 'carts'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout')
]
