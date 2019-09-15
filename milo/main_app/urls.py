
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup',views.signup,name='signup'),
    #path('profile/<int:profile_id>/add_photo/', views.add_photo, name='add_photo')
]
