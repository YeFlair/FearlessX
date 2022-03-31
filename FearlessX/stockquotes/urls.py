from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('search', views.search, name="search"),
    path('delete/<stock_id>', views.delete, name="delete"),
]
