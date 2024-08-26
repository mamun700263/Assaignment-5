from django.urls import path
from .views import RegistrationView,ProfileView,HomeView,LoginPage,CustomLogout
urlpatterns = [
    path('registration/',RegistrationView.as_view(),name='registration'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('login/',LoginPage.as_view(),name='login'),
    path('logout/',CustomLogout.as_view(),name='logout'),
]
