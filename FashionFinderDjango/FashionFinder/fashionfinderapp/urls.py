from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Look at views.py index() function and get that path
urlpatterns = [
    path('', views.index, name='index'),
    path('pieces/', views.pieces, name='pieces'),
    path('accounts/login/', views.login, name = 'login'),
    path('accounts/logout/', views.logout_view, name = 'logout'),
    path('accounts/register/', views.register, name = 'register'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('user/<int:user_id>/', views.user),
    path('users/<int:user_id>', views.user),
    path('upload/', views.predict),
    path('wardrobe/', views.wardrobe),
    path('async/wardrobe/', views.wardrobe_json),
    path('recommendations/', views.rec),
    path('recommendations/<piece_id>', views.rec_async),
    path('recommendations/complementary/<piece_id>', views.rec_comp),
    path('async/recommendations/<piece_id>', views.async_recommendations_json),
    path('async/recommendations/complementary/<piece_id>', views.async_recommendations_comp_json)

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
