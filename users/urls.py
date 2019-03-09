from django.urls import path
from .views import LoginView, RegisterView
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register')
]
