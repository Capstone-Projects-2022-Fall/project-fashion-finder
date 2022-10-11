from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.urls import include
from django.contrib import admin

# Look at views.py index() function and get that path
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('pieces', views.pieces, name='pieces'),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register),

]
