from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('hello/', views.say_hello),
    path('upload/', views.upload, name = 'upload')

]