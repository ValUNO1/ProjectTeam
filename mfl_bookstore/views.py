from django.shortcuts import render
from .models import *
from .forms import *

def upload_book(request):

	book = Book.objects.filter()
	return render(request, 'mfl_bookstore/upload_book.html', {'books': book})