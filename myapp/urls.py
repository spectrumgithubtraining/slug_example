# myapp/urls.py
from django.urls import path
from .views import my_model_detail

urlpatterns = [
    path('my-model/<slug:slug>/', my_model_detail, name='my_model_detail'),
]
