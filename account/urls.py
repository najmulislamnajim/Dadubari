from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.user_registration,name='register'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout'),
]
