
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    path('profile', views.profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup',views.signup,name='signup')
=======
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls'))
>>>>>>> 32d02e3c86866ad6366741ab561bbb1e5f3c6cf2
]
