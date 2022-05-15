from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('tv', views.tv, name='tv'),
    path('create_tv', views.create_tv, name='create_tv'),
    path('edit_tv', views.edit_tv, name='edit_tv'),
     path('tv_filtrated', views.tv_filtrated, name='tv_filtrated'),
    
    path('director', views.director, name='director'),
   

]