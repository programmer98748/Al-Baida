from django.urls import path, re_path
from . import views
from .views import (
    PageDeleteView,
    PageCreateView,
)

from django.contrib.auth.views import LogoutView

from django.contrib.auth import views as auth_views


app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
    path('informaion_site/', views.edite_informaion, name='informaion_site'),
    path('profile/', views.profile, name='profile'),
    path("logout/", views.auth_logout, name="logout"),
###
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/delete', views.delete, name='delete'),

###
    path('category/', views.category, name='category'),
    path('category/edite/<int:id>/', views.category_edite, name='category_edite'),
    path('category/delete/<int:id>/', views.category_delete, name='category_delete'),
    path('category/create/', views.category_add, name='category_add'),


##
    path('page/', views.page, name='page'),
    path('page/about', views.page_about, name='page_about'),

    path('page/create/', PageCreateView.as_view(), name='page_add'),
    path('page/edite/<int:id>/', views.page_edite, name='page_edite'),
 #   path('page/delete/<int:id>/', views.page_delete, name='page_delete'),
    path('page/delete/<int:pk>/', PageDeleteView.as_view(), name='page_delete'),

##
    path('aluser/<int:pk>', views.AEditUser.as_view(), name='user_edite'),
    path('aluser/', views.user_show, name='aluser'),
    path('create_use/', views.create_user, name='create_user_form'),
    path('alvuser/<int:pk>', views.ALViewUser.as_view(), name='alvuser'),
    path('aeuser/<int:pk>', views.AEditUser.as_view(), name='aeuser'),
    path('aduser/<int:pk>', views.ADeleteUser.as_view(), name='aduser'),
]