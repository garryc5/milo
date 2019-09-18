
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
    path('profile/<int:pk>/update/',
         views.ProfileUpdate.as_view(), name='profile_update'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
    path('profile/<int:profile_id>/add_photo/',
         views.add_photo, name='add_photo'),
<<<<<<< HEAD
    path('profile/activity/create/', views.ActivityCreate.as_view(), name='activity_create')
=======
    path('profile/activity/create/',
         views.ActivityCreate.as_view(), name='activity_create')
>>>>>>> ecc4ff60eefaaef31f44a75e032215aca3129e8c
]
