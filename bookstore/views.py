from django.shortcuts import render


def bookshelf(request):
    return render(request, 'bookstore/bookshelf.html', {'title': 'BookShelf'})

