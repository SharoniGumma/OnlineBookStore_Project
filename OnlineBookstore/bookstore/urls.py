from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('book/<int:book_id>/',views.book_detail,name='book_detail'),
    path('add_to_cart<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name="cart"),
    path('analytics/', views.analytics, name="analytics")
    
]
