from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.urls import path

from . import views

# Look at views.py index() function and get that path
urlpatterns = [
                  path('vote/', views.vote, name='vote'),
                  path('', views.index, name='index'),
                  path('pieces/', views.pieces, name='pieces'),
                  path('accounts/login/', views.login, name='login'),
                  path('accounts/logout/', views.logout_view, name='logout'),
                  path('accounts/register/', views.register, name='register'),

                  path('accounts/', include('django.contrib.auth.urls')),

                  path('user/<int:user_id>/', views.user),
                  path('users/<int:user_id>', views.user),
                  path('upload/', views.predict),
                  path('wardrobe/', views.wardrobe),
                  path('recommendations/', views.rec),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
