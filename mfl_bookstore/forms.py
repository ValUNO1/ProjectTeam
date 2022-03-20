from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('genre', 'author', 'coverpage', 'title', 'price', 'stock', 'status', 'description')