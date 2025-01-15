from django.urls import path
from user_auth.views import login_view, registration_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout')
]
