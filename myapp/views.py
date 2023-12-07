# myapp/views.py
from django.shortcuts import render, get_object_or_404
from .models import MyModel

def my_model_detail(request, slug):
    obj = get_object_or_404(MyModel, slug=slug)
    return render(request, 'myapp/my_model_detail.html', {'obj': obj})
