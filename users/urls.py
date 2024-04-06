from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('edit/', views.profile_edit, name='edit'),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]