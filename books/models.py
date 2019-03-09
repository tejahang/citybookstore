from django.db import models
from autoslug import AutoSlugField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    slug = AutoSlugField(populate_from='title')
    image = models.FileField(upload_to='photos')
    publisher = models.CharField(max_length=30)
    published_year = models.IntegerField()
    condition = models.CharField(max_length=10)
    cover_type = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.CharField(max_length=15)
    isbn = models.CharField(max_length=13)
    contact = models.CharField(max_length=10)
    description = models.TextField(max_length=500, blank=True)
    seller = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

    def short_name(self):
        if len(self.title) > 26:
            return self.title[:20] + '...' + self.title[-4:]

        return self.title



