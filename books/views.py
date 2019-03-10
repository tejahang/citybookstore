from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category, Book


# Create your views here.

class BaseView(View):
    context = {
        'categories': Category.objects.order_by('-id')
    }


class HomeView(BaseView):
    def get(self, request):
        self.context['latest_uploads'] = Book.objects.order_by('-id')[:6]
        self.context['top_trending'] = Book.objects.order_by('?')[:5]
        self.context['new_releases'] = Book.objects.order_by('id')[:7]
        return render(request, 'pages/index.html', self.context)


class SellView(LoginRequiredMixin, BaseView):
    def get(self, request):
        return render(request, 'pages/sell.html', self.context)

    def post(self, request):
        title = request.POST['title']
        seller = request.POST['seller']
        author = request.POST['author']
        price = request.POST['price']
        publisher = request.POST['publisher']
        published_year = request.POST['year']
        condition = request.POST['condition']
        cover_type = request.POST['cover']
        category = request.POST['category']
        cat = Category.objects.get(name=category)
        language = request.POST['language']
        isbn = request.POST.get('isbn')
        description = request.POST.get('description')
        myfile = request.FILES.get('image')
        contact = request.POST.get('contact')

        book = Book(contact=contact, seller=seller, title=title, author=author, price=price, image=myfile,
                    publisher=publisher,
                    published_year=published_year, condition=condition, cover_type=cover_type, category=cat,
                    language=language, isbn=isbn, description=description)
        book.save()
        return redirect('books:index')


class WorksView(BaseView):
    def get(self, request):
        return render(request, 'pages/how-it-works.html')


class CategoryWiseView(BaseView):
    def get(self, request, category_slug):
        self.context['category_wise'] = Category.objects.get(slug=category_slug)
        return render(request, 'pages/category_wise.html', self.context)


class SingleWiseView(BaseView):
    def get(self, request, book_slug):
        self.context['book'] = Book.objects.get(slug=book_slug)
        self.context['top_trending'] = Book.objects.order_by('?')[:5]
        return render(request, 'pages/single-book.html', self.context)


class SearchView(BaseView):
    def get(self, request):
        q = request.GET.get('q', None)
        if not q:
            return redirect('/')

        self.context['search_results'] = Book.objects.filter(title__icontains=q)
        return render(request, 'pages/search-results.html', self.context)
