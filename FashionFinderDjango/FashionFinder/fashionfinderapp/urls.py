from django.urls import path

from . import views

# Look at views.py index() function and get that path
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('pieces', views.pieces, name='pieces'),
]
