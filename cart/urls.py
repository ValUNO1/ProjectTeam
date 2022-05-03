from django.urls import path, include
from . import views

app_name = 'cart'

urlpatterns = [
    path('detail', views.cart_detail, name='cart_detail'),
    path('add/<int:book_id>/',
         views.cart_add,
         name='cart_add'),
    path('remove/<int:book_id>/',
         views.cart_remove,
         name='cart_remove'),

    path('password/', views.change_password, name='change_password'),
]