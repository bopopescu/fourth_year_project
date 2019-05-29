from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register.as_view(), name='register'),
    path('apiconnect/', views.apiconnect, name='apiconnect'),
    path('forex/', views.forex, name='forex'),
    path('crypto/', views.crypto, name='crypto'),
    path('about/', views.about, name='about'),
    path('secret/', views.secret_page, name='secret'),
    path('maketradeforex/', views.maketradeforex, name='maketradeforex'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sentiment/', views.sentiment, name='sentiment'),
    path('cryptodashboard/', views.cryptodashboard, name='cryptodashboard'),
    path('forexdashboard/', views.forexdashboard, name='forexdashboard'),
]
