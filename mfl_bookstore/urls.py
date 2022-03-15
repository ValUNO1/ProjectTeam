from django.urls import path
from . import views

app_name = "mfl_bookstore"


urlpatterns = [
    path("homepage", views.homepage, name="homepage"),
    #...
    path("register", views.register_request, name="registration")
]