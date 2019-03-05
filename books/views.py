from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class BaseView(View):
    def get(self, request):
        return render(request, 'pages/index.html')


class SellView(LoginRequiredMixin, BaseView):
    def get(self, request):
        return render(request, 'pages/sell.html')


class WorksView(BaseView):
    def get(self, request):
        return render(request, 'pages/how-it-works.html')


class CartView(LoginRequiredMixin, BaseView):
    def get(self, request):
        return render(request, 'pages/cart.html')


class CategoryWiseView(BaseView):
    def get(self, request):
        return render(request, 'pages/category_wise.html')
