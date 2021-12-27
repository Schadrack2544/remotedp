from django.urls import path
from . import views

urlpatterns = [
    path('personal_info/', views.personal_info, name='personal_info'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login_success/', views.login_success, name='login_success'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('transcript/',views.transcript, name='transcript'),
    path('pay/', views.pay, name='pay'),
    path('', views.home, name='home'),
    
]