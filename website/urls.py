from django.urls import path

from . import views 
urlpatterns = [
    path('', views.index, name='websitehome'),
    path('project/<str:slug>/', views.portfolio_details , name='portfolio_details'),
    path('contact', views.contact , name='contact'),
    path('about', views.about , name='about'),
    path('portfolio', views.portfolio , name='portfolio'),
    path('filter-images/', views.filter_images, name='filter_images'),


]