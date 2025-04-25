
from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('order/<int:id>/', views.order_view, name='order'),
    path('customorder', views.custom_order, name='custom_order'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/delete/<int:order_id>/', views.delete_order, name='delete_order'),
]
