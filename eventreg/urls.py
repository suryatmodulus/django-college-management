from django.urls import path
from eventreg import views



urlpatterns = [
    path('', views.EventsView, name='events'),
    path('register/', views.RegView, name='register'),
    path('success/', views.SuccessView, name='success'),
    path('regerror/', views.ErrorView, name='regerror'),
    path('check/', views.CheckView, name='check'),
    path('result/', views.ResultView, name='result'),
]