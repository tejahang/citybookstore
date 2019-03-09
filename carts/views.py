from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart
from django.contrib import messages


# Create your views here.

class CartView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'my_cart': Cart.objects.filter(user_id=request.user.id)
        }
        return render(request, 'pages/cart.html', context)

    def post(self, request):
        name = request.POST['book']
        price = request.POST['price']
        user_id = request.POST['user_id']
        image = request.POST['image']

        cart = Cart(book=name, price=price, user_id=user_id, image=image)
        cart.save()

        return redirect('carts:cart')


class CheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'my_cart': Cart.objects.filter(user_id=request.user.id)
        }
        return render(request, 'pages/cart.html', context)

    def post(self, request):
        items = Cart.objects.filter(user_id=request.user.id)
        items.delete()
        messages.success(request, 'Thank you for shopping with Books Bay. Your books will be delivered shortly.')
        return redirect('books:index')
