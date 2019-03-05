from django.urls import path
from .views import BaseView, SellView, WorksView, CartView

app_name = 'books'

urlpatterns = [
    path('', BaseView.as_view(), name='index'),
    path('sell/', SellView.as_view(), name='sell-my-book'),
    path('how-it-works/', WorksView.as_view(), name='how-it-works'),
    path('cart/', CartView.as_view(), name='cart'),
    # path('category/<str:category_slug>', CategoryWiseView.as_view(), name='category-wise')
]
