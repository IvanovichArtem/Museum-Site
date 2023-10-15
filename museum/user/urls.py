from django.urls import path
from .views import login, registration, logout, profile

app_name = 'user'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('logout', logout, name='logout'),
    path('profile', profile, name='profile')
]