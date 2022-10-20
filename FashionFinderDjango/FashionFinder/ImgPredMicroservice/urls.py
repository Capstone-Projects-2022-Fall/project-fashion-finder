from django.urls import path

from . import views

# Look at views.py index() function and get that path
urlpatterns = [
    path('', views.index, name='index'),
    path('predict', views.predict, name='predict')
]
