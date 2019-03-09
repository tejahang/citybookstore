from django.db import models
from books.models import Book


# Create your models here.


class Cart(models.Model):
    book = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    user_id = models.IntegerField(blank=True)
    image = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.book
