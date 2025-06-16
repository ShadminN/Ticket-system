from django.urls import path
from . import views

urlpatterns = [
    path('tickets', views.ticket_list, name='ticket'),
    path('users', views.user_list, name='users'),
    path('category', views.category_list, name='category'),
    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('contact', views.contact, name='contact'),
]
