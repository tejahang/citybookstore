from django.urls import path
from .views import HomeView, SellView, WorksView, CategoryWiseView, SingleWiseView, SearchView

app_name = 'books'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('sell/', SellView.as_view(), name='sell-my-book'),
    path('how-it-works/', WorksView.as_view(), name='how-it-works'),
    path('category/<str:category_slug>', CategoryWiseView.as_view(), name='category-wise'),
    path('book/<str:book_slug>', SingleWiseView.as_view(), name='single-book-wise'),
    path('search/', SearchView.as_view(), name='search'),
]
