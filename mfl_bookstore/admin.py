from django.contrib import admin
from .models import Genre, Author, Book


# Register your models here.
class AddGenre(admin.ModelAdmin):
    list_display = ['type']

admin.site.register(Genre, AddGenre)


class AddAuthor(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Author, AddAuthor)


class AddBook(admin.ModelAdmin):
    list_display = ['title', 'price', 'stock', 'status', 'created', 'updated']
    list_filter = ['status', 'created', 'updated']
    list_editable = ['price', 'stock', 'status']

admin.site.register(Book, AddBook)