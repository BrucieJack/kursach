from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('tv', views.tv, name='tv'),
    path('create_tv', views.create_tv, name='create_tv'),
    path('tv_filtrated', views.tv_filtrated, name='tv_filtrated'),
    path('tv_search', views.tv_search, name='tv_search'),
    
    path('director', views.director, name='director'),
    path('director_filtrated', views.director_filtrated, name='director_filtrated'),
    path('director_search', views.director_search, name='director_search'),

    path('method', views.method, name='method'),

]