from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.index, name='index'),
    path('products/<int:pk>/', views.show, name='show'),
]
