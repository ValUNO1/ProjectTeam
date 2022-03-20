from django.urls import path
from . import views

app_name = "mfl_bookstore"


urlpatterns = [
    path('', views.upload_book, name='upload_book'),
    path('upload_book', views.upload_book, name='upload_book'),
]