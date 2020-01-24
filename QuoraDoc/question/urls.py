from django.contrib import admin
from django.urls import path
from .views import RegisterView

app_name = "question"

urlpatterns = [
    path('register/', views.RegisterView, name='register-view'),
]