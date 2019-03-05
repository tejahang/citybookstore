from django.urls import path
from .views import HomeView, SellView, WorksView, CartView, CategoryWiseView, SingleWiseView

app_name = 'books'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('sell/', SellView.as_view(), name='sell-my-book'),
    path('how-it-works/', WorksView.as_view(), name='how-it-works'),
    path('cart/', CartView.as_view(), name='cart'),
    path('category/<str:category_slug>', CategoryWiseView.as_view(), name='category-wise'),
    path('product/<str:book_slug>', SingleWiseView.as_view(), name='single-book-wise')
]
